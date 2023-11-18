from django.contrib import admin

# Register your models here.

from .models import UserProfile, Team, TeamPlayer, Player, Match, Result, Leaderboard



admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(TeamPlayer)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Result)
admin.site.register(Leaderboard)
    