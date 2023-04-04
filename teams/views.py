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

        except NegativeTitlesError or InvalidYearCupError or ImpossibleTitlesError as err:
            return Response(
                {"error": err.message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(team_dict, status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
            team_dict = model_to_dict(team)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(team_dict, status=status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)

            for key, value in request.data.items():
                setattr(team, key, value)

            team.save()
            team_dict = model_to_dict(team)

        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(team_dict, status=status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
