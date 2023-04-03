from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from teams.exceptions import (
    ImpossibleTitlesError,
    InvalidYearCupError,
    NegativeTitlesError,
)

from teams.models import Team
from .utils import data_processing

# Create your views here.
class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_list = [model_to_dict(team) for team in teams]
        return Response(teams_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            data = request.data
            validate = data_processing(data)
            team = Team.objects.create(**validate)
            team_dict = model_to_dict(team)

        except NegativeTitlesError as err:
            return Response(
                {"error": err.message},
                status.HTTP_400_BAD_REQUEST,
            )
        except InvalidYearCupError as err:
            return Response(
                {"error": err.message},
                status.HTTP_400_BAD_REQUEST,
            )
        except ImpossibleTitlesError as err:
            return Response(
                {"error": err.message},
                status.HTTP_400_BAD_REQUEST,
            )

        return Response(team_dict, status.HTTP_201_CREATED)
