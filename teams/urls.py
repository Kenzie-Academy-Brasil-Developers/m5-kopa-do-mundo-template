from django.urls import path
from teams.views import TeamView

urlpatterns = [
    path("teams/", TeamView.as_view()),
]
