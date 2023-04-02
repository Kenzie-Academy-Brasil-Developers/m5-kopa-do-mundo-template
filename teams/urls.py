from kopa_do_mundo.urls import path
from django.urls import path
from teams.views import TeamDetailView, TeamsView

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<team_id>/", TeamDetailView.as_view())
]
