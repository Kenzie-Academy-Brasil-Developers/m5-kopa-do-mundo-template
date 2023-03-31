from django.urls import path
from teams.views import TeamView, TeamDetailView

urlpatterns = [    
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamDetailView.as_view()),
]
