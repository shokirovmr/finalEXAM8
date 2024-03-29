from django.db import models


# class Player(models.Model):
#     name = models.CharField(max_length=100)
#

class Team(models.Model):
    name = models.CharField(max_length=100)


class Match(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)

class MatchSummary(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)



class PlayerMatchPoint(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    points = models.IntegerField()


class PointDescription(models.Model):
    description = models.CharField(max_length=100)


class Fixture(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)


class UserTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class UserTeamPlayer(models.Model):
    user_team = models.ForeignKey(UserTeam, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


class League(models.Model):
    name = models.CharField(max_length=100)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    content = models.TextField()


class PlayerStatistics(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
