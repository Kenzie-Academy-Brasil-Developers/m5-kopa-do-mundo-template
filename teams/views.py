from rest_framework.views import APIView, status, Request, Response
from teams.models import Team
from django.forms import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, ImpossibleTitlesError, InvalidYearCupError


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        try:
            received_data = data_processing(request.data)
            team = Team.objects.create(**received_data)
            converted_team = model_to_dict(team)
            return Response(converted_team, status.HTTP_201_CREATED)
        except (
            NegativeTitlesError,
            ImpossibleTitlesError,
            InvalidYearCupError,
        ) as err:
            return Response({"error": err.args[0]}, status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        converted_teams = [model_to_dict(team) for team in teams]
        return Response(converted_teams)


