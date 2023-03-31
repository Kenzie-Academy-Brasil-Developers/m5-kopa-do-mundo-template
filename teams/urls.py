from django.urls import path
from .views import TeamsView, TeamDetailsView


urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", TeamDetailsView.as_view())
]
