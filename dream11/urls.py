"""
URL configuration for dream11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from datarepo.views import (
    user_profile_api, team_api, player_api, match_api, result_api, teams_api,
    players_api, matches_api, results_api, team_players_api, leaderboards_api,
    user_profiles_api,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # APIs with ID in URL
    path('user-profile/<int:user_id>/', user_profile_api, name='user-profile-api'),
    path('team/<int:team_id>/', team_api, name='team-api'),
    path('player/<int:player_id>/', player_api, name='player-api'),
    path('match/<int:match_id>/', match_api, name='match-api'),
    path('result/<int:match_id>/', result_api, name='result-api'),

    # APIs to get all data
    path('user-profiles/', user_profiles_api, name='user-profiles-api'),
    path('teams/', teams_api, name='teams-api'),
    path('players/', players_api, name='players-api'),
    path('matches/', matches_api, name='matches-api'),
    path('results/', results_api, name='results-api'),
    path('team-players/', team_players_api, name='team-players-api'),
    path('leaderboards/', leaderboards_api, name='leaderboards-api'),
]

