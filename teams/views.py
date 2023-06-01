from django.forms import model_to_dict
from rest_framework.views import APIView, Request, Response, status
from exceptions import *
from utils import data_processing
from .models import Team


class TeamsView(APIView):
    def post(self, request: Request) -> Response:
        try:
            info_selection = request.data
            data_processing(info_selection)
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"msg": f"{err.message}"}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)
        return Response(teams_list, status.HTTP_200_OK)


class TeamsIdView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)
