from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status

from teams.exceptions import ImpossibleTitlesError, InvalidYearCupError
from teams.exceptions import NegativeTitlesError
from .models import Team
from django.forms.models import model_to_dict
from teams.utils import data_processing


# Create your views here.
class TeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        if len(teams_list) <= 0:
            return Response("item vazio",  status.HTTP_404_NOT_FOUND)

        return Response(teams_list, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        try:
            print(data_processing(request.data))
            team = Team.objects.create(**request.data)
            team_dict = model_to_dict(team)
            return Response(team_dict, status.HTTP_201_CREATED)
        except InvalidYearCupError as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        except NegativeTitlesError as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
    # def delete(self, request: Request):

        