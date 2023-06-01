from django.urls import path
from .views import *

urlpatterns = [path("teams/", TeamsView.as_view())]
