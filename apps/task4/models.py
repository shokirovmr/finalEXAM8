from django.db import models


class Championship(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    # championship = models.ForeignKey(Championship, related_name='championship_name', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Match(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateField()
    home_team_score = models.PositiveIntegerField()
    away_team_score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}, {self.date}"


class MatchStatistic(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    home_team_possession = models.FloatField()
    away_team_possession = models.FloatField()
    home_team_goal_attempts = models.PositiveIntegerField()
    away_team_goal_attempts = models.PositiveIntegerField()
    home_team_shots_on_goal = models.PositiveIntegerField()
    away_team_shots_on_goal = models.PositiveIntegerField()
    home_team_shots_off_goal = models.PositiveIntegerField()
    away_team_shots_off_goal = models.PositiveIntegerField()
    home_team_free_kicks = models.PositiveIntegerField()
    away_team_free_kicks = models.PositiveIntegerField()
    home_team_corner_kicks = models.PositiveIntegerField()
    away_team_corner_kicks = models.PositiveIntegerField()
    home_team_offsides = models.PositiveIntegerField()
    away_team_offsides = models.PositiveIntegerField()
    home_team_throw_ins = models.PositiveIntegerField()
    away_team_throw_ins = models.PositiveIntegerField()
    home_team_goalkeeper_saves = models.PositiveIntegerField()
    away_team_goalkeeper_saves = models.PositiveIntegerField()
    home_team_fouls = models.PositiveIntegerField()
    away_team_fouls = models.PositiveIntegerField()
    home_team_tackles = models.PositiveIntegerField()
    away_team_tackles = models.PositiveIntegerField()
    home_team_attacks = models.PositiveIntegerField()
    away_team_attacks = models.PositiveIntegerField()
    home_team_dangerous_attacks = models.PositiveIntegerField()
    away_team_dangerous_attacks = models.PositiveIntegerField()
    home_team_clearances_completed = models.PositiveIntegerField()
    away_team_clearances_completed = models.PositiveIntegerField()
    home_team_yellow_cards = models.PositiveIntegerField()
    away_team_yellow_cards = models.PositiveIntegerField()
    home_team_red_cards = models.PositiveIntegerField()
    away_team_red_cards = models.PositiveIntegerField()
    home_team_total_passes = models.PositiveIntegerField()
    away_team_total_passes = models.PositiveIntegerField()

    def __str__(self):
        return f"Match Statistic for {self.match}"


class Player(models.Model):
    player_name = models.CharField(max_length=30)
    player_age = models.PositiveIntegerField()
    player_nationality = models.CharField(max_length=20)
    player_position = models.CharField(max_length=15)
    player_team = models.ForeignKey(Team, related_name="player_name", on_delete=models.CASCADE)
    player_yellow_cards = models.PositiveIntegerField()
    player_red_cards = models.PositiveIntegerField()
    contract_expires = models.DateField()

    def __str__(self):
        return self.player_name


class Title(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Coach(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    number_of_managed_clubs = models.PositiveIntegerField()
    titles_won = models.ManyToManyField(Title, related_name='title_coach')

    def __str__(self):
        return self.name


class Standings(models.Model):
    team_name = models.ForeignKey(Team, related_name='team_standing_name', on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
    matches_played = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)
    win = models.PositiveIntegerField(default=0)
    goal_diff = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Standings'
        verbose_name_plural = 'Standings'

    def __str__(self):
        return self.team_name


class TopScorers(models.Model):
    player = models.ForeignKey(Player, related_name='player_topscorer', on_delete=models.DO_NOTHING)
    goals = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Top Scorers'
        verbose_name_plural = 'Top Scorers'

    def __str__(self):
        return self.player


class Transfermarket(models.Model):
    player_name = models.ForeignKey('Player', related_name='player_transfermarket', on_delete=models.CASCADE)
    market_value = models.PositiveIntegerField()
    from_club = models.ForeignKey('Team', related_name='transfers_out', on_delete=models.CASCADE)
    to_club = models.ForeignKey('Team', related_name="transfers_in", on_delete=models.CASCADE)
    age = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Transfer Market'
        verbose_name_plural = 'Transfer Market'

    def __str__(self):
        return str(self.player_name)
