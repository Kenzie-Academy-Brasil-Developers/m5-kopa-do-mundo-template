from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from .models import Team


class TeamView(APIView):
    def post(self, request):
        try:
            data_processing(request.data)

            team = Team.objects.create(**request.data)
            team_dict = model_to_dict(team)
        
            return Response(team_dict, status.HTTP_201_CREATED)
        
        except (NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError) as err:
            return Response({"error": str(err)}, 400)

    def get(self, request):
        teams = Team.objects.all()
        team_dict = []

        for team in teams:
            t = model_to_dict(team)
            team_dict.append(t)

        return Response(team_dict, status.HTTP_200_OK)
    

class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)
    
    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()

            return Response(status.HTTP_204_NO_CONTENT)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
    def update(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)

            for i, value in request.data.items():
                setattr(team, i, value)

            team.save()
            team_dict = model_to_dict(team)

            return Response(team_dict, status.HTTP_200_OK)

        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
