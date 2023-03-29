from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team
from .utils import data_processing
from .exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        list_teams = []
        for team in teams:
            list_team_dict = model_to_dict(team)
            list_teams.append(list_team_dict)
        return Response(list_teams, status.HTTP_200_OK)

    def post(self, request):
        try:
            data_processing(**request.data)
        except NegativeTitlesError as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)
        new_team = Team.objects.create(**request.data)
        team_dict = model_to_dict(new_team)
        return Response(team_dict, status.HTTP_201_CREATED)

