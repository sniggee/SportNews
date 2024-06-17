from django.db import models
from common.models import BasketballTeam, FootballTeam, HockeyTeam


class Match(models.Model):
    stage = models.CharField(max_length=100)
    match_title = models.CharField(max_length=255)
    game_id = models.CharField(max_length=100, unique=True)
    time = models.CharField(max_length=50)
    home_logo_url = models.URLField()
    away_logo_url = models.URLField()
    home_goals = models.CharField(max_length=10)
    away_goals = models.CharField(max_length=10)

    def __str__(self):
        return self.match_title


class ManualMatch(models.Model):
    title = models.CharField("название турнира", max_length=255)
    time = models.CharField("время начала матча", max_length=50)
    one_name_command = models.CharField("название 1 команды", max_length=255)
    one_logo_command = models.URLField("логотип 1 команды")
    two_name_command = models.CharField("название 2 команды", max_length=255)
    two_logo_command = models.URLField("логотип 2 команды")
    home_goals = models.CharField("гол 1 команды", max_length=10, default="-")
    away_goals = models.CharField("гол 2 команды", max_length=10, default="-")
    stage = models.CharField("Номер турнира", max_length=100)

    def __str__(self):
        return self.title


class TeamResult(models.Model):
    team = models.ForeignKey(FootballTeam, on_delete=models.SET_NULL, null=True, verbose_name="Комманда")
    matches = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    goalsFor = models.PositiveIntegerField()
    goalsAgainst = models.PositiveIntegerField()
    goalDifference = models.CharField(max_length=10)
    points = models.PositiveIntegerField()

    class Meta:
        abstract = True


class FootbalResult(TeamResult):
    draws = models.PositiveIntegerField()

    class Meta:
        ordering = ["-points"]
        verbose_name = "Результаты футбол"
        verbose_name_plural = "Результаты футбол"


class BasketballResult(models.Model):
    team = models.ForeignKey(BasketballTeam, on_delete=models.SET_NULL, null=True, verbose_name="Комманда")
    matches = models.PositiveIntegerField()
    goalsFor = models.PositiveIntegerField()
    goalsMissed = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    looses = models.PositiveIntegerField()
    total_points = models.PositiveIntegerField()

    class Meta:
        ordering = ["-total_points"]
        verbose_name = "Результаты баскетбол"
        verbose_name_plural = "Результаты баскетбол"


class HockeyResult(models.Model):
    team = models.ForeignKey(HockeyTeam, on_delete=models.SET_NULL, null=True, verbose_name="Комманда")
    matches = models.PositiveIntegerField()
    goalsFor = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    goalsMissed = models.PositiveIntegerField()
    looses = models.PositiveIntegerField()
    

    class Meta:
        ordering = ["-points"]
        verbose_name = "Результаты хоккей"
        verbose_name_plural = "Результаты хоккей"
