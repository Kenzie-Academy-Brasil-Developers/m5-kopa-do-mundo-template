from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from .models import Team
from .utils import data_processing
from .exceptions import InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError


class TeamView(APIView):
    def post(self, request: Request):
        try:
            team_data = request.data
            data_processing(team_data)
            team = Team.objects.create(
                name=team_data["name"],
                titles=team_data["titles"],
                top_scorer=team_data["top_scorer"],
                fifa_code=team_data["fifa_code"],
                first_cup=team_data["first_cup"],
            )
            team_dict = model_to_dict(team)

            return Response(team_dict, status.HTTP_201_CREATED)
        except NegativeTitlesError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        teams = Team.objects.all()

        team_dict = [model_to_dict(team) for team in teams]

        return Response(team_dict, status.HTTP_200_OK)


class TeamDetailView(APIView):
    def get(self, request: Request, id):
        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team_dict = model_to_dict(team)

        return Response(team_dict)

    def patch(self, request: Request, id):
        try:
            team = Team.objects.get(pk=id)
            request_data = request.data

            for key, value in request_data.items():
                setattr(team, key, value)

            team.save()
            return Response(model_to_dict(team), status.HTTP_200_OK)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        except NegativeTitlesError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            return Response({"error": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id):
        try:
            team = Team.objects.get(pk=id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
