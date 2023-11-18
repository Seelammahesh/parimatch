from django.db import models
from django.contrib.auth.models import AbstractUser,User


class UserProfile(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Team(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=255)
    total_points = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)
    points_earned = models.IntegerField(default=0)

    def __str__(self):
        return self.player_name


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    winner_team = models.ForeignKey(Team, related_name='winner_team', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Upcoming', 'Upcoming'), ('Live', 'Live'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.status}"


class Result(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    team1_points = models.IntegerField()
    team2_points = models.IntegerField()

    def __str__(self):
        return f"Result for {self.match}"


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team.team_name} - {self.player.player_name}"


class Leaderboard(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    points_earned = models.IntegerField()

    def __str__(self):
        return f"{self.user.user.username} - {self.match} - {self.points_earned}"
