from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Team, Player, Match, Result, TeamPlayer, Leaderboard

# APIs with ID in URL

# User Profile API
@api_view(['GET'])
@login_required
def user_profile_api(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    data = {
        'username': user_profile.username,
        'balance': user_profile.balance,
        'registration_date': user_profile.registration_date,
        'last_login_date': user_profile.last_login_date,
    }
    return Response(data)


# Team API
@api_view(['GET'])
@login_required
def team_api(request, team_id):
    team = get_object_or_404(Team, id=team_id, user=request.user)
    data = {
        'team_name': team.team_name,
        'total_points': team.total_points,
        'creation_date': team.creation_date,
    }
    return Response(data)


# Player API
@api_view(['GET'])
def player_api(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    data = {
        'player_name': player.player_name,
        'team_name': player.team.team_name,
        'position': player.position,
        'points_earned': player.points_earned,
    }
    return Response(data)


# Match API
@api_view(['GET'])
def match_api(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    data = {
        'team1': match.team1.team_name,
        'team2': match.team2.team_name,
        'match_date': match.match_date,
        'winner_team': match.winner_team.team_name if match.winner_team else None,
        'status': match.status,
    }
    return Response(data)


# Result API
@api_view(['GET'])
def result_api(request, match_id):
    result = get_object_or_404(Result, match_id=match_id)
    data = {
        'team1_points': result.team1_points,
        'team2_points': result.team2_points,
    }
    return Response(data)


# APIs to get all data

# User Profiles API
@api_view(['GET'])
@login_required
def user_profiles_api(request):
    user_profiles = UserProfile.objects.all()
    data = [{'username': profile.username, 'balance': profile.balance, 'registration_date': profile.registration_date, 'last_login_date': profile.last_login_date} for profile in user_profiles]
    return Response(data)


# Teams API
@api_view(['GET'])
@login_required
def teams_api(request):
    teams = Team.objects.filter(user=request.user)
    data = [{'team_name': team.team_name, 'total_points': team.total_points, 'creation_date': team.creation_date} for team in teams]
    return Response(data)


# Players API
@api_view(['GET'])
def players_api(request):
    players = Player.objects.all()
    data = [{'player_name': player.player_name, 'team_name': player.team.team_name, 'position': player.position, 'points_earned': player.points_earned} for player in players]
    return Response(data)


# Matches API
@api_view(['GET'])
def matches_api(request):
    matches = Match.objects.all()
    data = [{'team1': match.team1.team_name, 'team2': match.team2.team_name, 'match_date': match.match_date,
             'winner_team': match.winner_team.team_name if match.winner_team else None, 'status': match.status} for match in matches]
    return Response(data)


# Results API
@api_view(['GET'])
def results_api(request):
    results = Result.objects.all()
    data = [{'team1_points': result.team1_points, 'team2_points': result.team2_points} for result in results]
    return Response(data)


# TeamPlayers API
@api_view(['GET'])
def team_players_api(request):
    team_players = TeamPlayer.objects.all()
    data = [{'team_name': tp.team.team_name, 'player_name': tp.player.player_name, 'position': tp.player.position} for
            tp in team_players]
    return Response(data)

# Leaderboards API
@api_view(['GET'])
def leaderboards_api(request):
    leaderboard_entries = Leaderboard.objects.all().order_by('-points_earned')
    data = [{'username': entry.user.user.username, 'match_id': entry.match.id, 'points_earned': entry.points_earned} for entry in leaderboard_entries]
    return Response(data)

