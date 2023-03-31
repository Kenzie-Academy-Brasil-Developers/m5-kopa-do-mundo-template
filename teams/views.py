from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from .models import Team
from django.forms.models import model_to_dict
from .utils import data_processing
from .exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

# Create your views here.

class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = [model_to_dict(team) for team in teams]

        return Response(teams_list)
    
    def post(self, request: Request) -> Response:

        try:
            data_processing(request.data)
            team = Team.objects.create(**request.data)
        except NegativeTitlesError as err:
            return Response(err.message, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as err:
            return Response(err.message, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as err:
            return Response(err.message, status.HTTP_400_BAD_REQUEST)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)
