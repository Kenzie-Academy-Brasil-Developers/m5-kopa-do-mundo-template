from rest_framework.views import APIView, Response, Request, status
from teams.models import Team
from django.forms.models import model_to_dict
from .utils import data_processing
from .exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from django.db import IntegrityError


class TeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        team_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            team_list.append(team_dict)
        return Response(team_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)
            team = Team.objects.create(**request.data)
            print(model_to_dict(team))
            team_dict = model_to_dict(team)
            return Response(team_dict, status.HTTP_201_CREATED)
        except NegativeTitlesError:
            return Response(
                {"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST
            )
        except InvalidYearCupError:
            return Response(
                {"error": "there was no world cup this year"},
                status.HTTP_400_BAD_REQUEST,
            )
        except ImpossibleTitlesError:
            return Response(
                {"error": "impossible to have more titles than disputed cups"},
                status.HTTP_400_BAD_REQUEST,
            )
        except IntegrityError:
            return Response({"error": "ABREVIACO DE TIME"}, status.HTTP_400_BAD_REQUEST)


class TeamDetailsView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team_dict = model_to_dict(team)
            return Response(team_dict, status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            for key, value in request.data.items():
                setattr(team, key, value)
            team.save()
            team_dict = model_to_dict(team)
            return Response(team_dict, status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
