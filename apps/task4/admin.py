from django.contrib import admin

from apps.task4.models import Championship, Team, Match, MatchStatistic, Player, Coach, Standings, TopScorers, \
    Transfermarket, Title


@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(MatchStatistic)
class MatchStatisticAdmin(admin.ModelAdmin):
    pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass

@admin.register(Standings)
class StandingsAdmin(admin.ModelAdmin):
    pass

@admin.register(TopScorers)
class TopScorersAdmin(admin.ModelAdmin):
    pass

@admin.register(Transfermarket)
class TransfermarketAdmin(admin.ModelAdmin):
    pass

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    pass