from django.db import models
from common.models import BasketballTeam, FootballTeam, HockeyTeam


class ScheduleMatchBase(models.Model):
    date = models.DateField(verbose_name="Дата проведения матча")
    time = models.TimeField(verbose_name="Время проведения матча")

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_team.name + " x " + self.second_team.name


class ScheduleFootball(ScheduleMatchBase):
    first_team = models.ForeignKey(
        FootballTeam, verbose_name="Комманда 1", on_delete=models.SET_NULL, null=True, related_name="schedules1"
    )
    second_team = models.ForeignKey(
        FootballTeam, verbose_name="Комманда 2", on_delete=models.SET_NULL, null=True, related_name="schedules2"
    )

    class Meta:
        ordering = ["date", "time"]
        verbose_name = "Футбольный матч"
        verbose_name_plural = "Футбольные матчи"


class ScheduleHockey(ScheduleMatchBase):
    first_team = models.ForeignKey(
        HockeyTeam, verbose_name="Комманда 1", on_delete=models.SET_NULL, null=True, related_name="schedules1"
    )
    second_team = models.ForeignKey(
        HockeyTeam, verbose_name="Комманда 2", on_delete=models.SET_NULL, null=True, related_name="schedules2"
    )

    class Meta:
        ordering = ["date", "time"]
        verbose_name = "Хоккейный матч"
        verbose_name_plural = "Хоккейные матчи"


class ScheduleBassketball(ScheduleMatchBase):
    first_team = models.ForeignKey(
        BasketballTeam, verbose_name="Комманда 1", on_delete=models.SET_NULL, null=True, related_name="schedules1"
    )
    second_team = models.ForeignKey(
        BasketballTeam, verbose_name="Комманда 2", on_delete=models.SET_NULL, null=True, related_name="schedules2"
    )

    class Meta:
        ordering = ["date", "time"]
        verbose_name = "Баскетбольный матч"
        verbose_name_plural = "Баскетбольные матчи"
