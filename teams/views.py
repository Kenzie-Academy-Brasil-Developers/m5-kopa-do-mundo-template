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
            team = Team.objects.create(**data)
            team_dict = model_to_dict(team)
            data_processing(team_dict)

            return Response(team_dict, status.HTTP_201_CREATED)

        except NegativeTitlesError:
            return Response(
                {"error": "titles cannot be negative"},
                status.HTTP_400_BAD_REQUEST,
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
