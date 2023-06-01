from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from utils import data_processing


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)
        except Exception as e:
            message_error = str(e)
            return Response({"error": message_error}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = [model_to_dict(team) for team in teams]

        return Response(teams_dict)
