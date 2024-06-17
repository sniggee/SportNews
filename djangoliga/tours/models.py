from django.db import models
from schedule.models import ScheduleBassketball, ScheduleFootball, ScheduleHockey


class Tour(models.Model):
    num_of_tour = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"Тур {self.num_of_tour}"


class FootballTour(Tour):
    class Meta:
        verbose_name = "Тур по футболлу"
        verbose_name_plural = "Туры по футболлу"


class BasketballTour(Tour):
    class Meta:
        verbose_name = "Тур по баскетболу"
        verbose_name_plural = "Туры по баскетболу"


class HockeyTour(Tour):
    class Meta:
        verbose_name = "Тур по хоккею"
        verbose_name_plural = "Туры по хоккею"


class TourMatch(models.Model):
    score = models.CharField(verbose_name="счет", null=True, blank=True, max_length=10)

    class Meta:
        abstract = True


class FootballTourMatch(TourMatch):
    match = models.ForeignKey(ScheduleFootball, on_delete=models.SET_NULL, null=True, verbose_name="Матч")
    tour = models.ForeignKey(
        FootballTour, on_delete=models.SET_NULL, null=True, verbose_name="Тур", related_name="matches"
    )

    class Meta:
        verbose_name = "Матч тура по футболу"
        verbose_name_plural = "Матчи тура по футболу"


class BasketballTourMatch(TourMatch):
    match = models.ForeignKey(ScheduleBassketball, on_delete=models.SET_NULL, null=True, verbose_name="Матч")
    tour = models.ForeignKey(
        BasketballTour, on_delete=models.SET_NULL, null=True, verbose_name="Тур", related_name="matches"
    )

    class Meta:
        verbose_name = "Матч тура по баскетболу"
        verbose_name_plural = "Матчи тура по баскетболу"


class HockeyTourMatch(TourMatch):
    match = models.ForeignKey(ScheduleHockey, on_delete=models.SET_NULL, null=True, verbose_name="Матч")
    tour = models.ForeignKey(
        HockeyTour, on_delete=models.SET_NULL, null=True, verbose_name="Тур", related_name="matches"
    )

    class Meta:
        verbose_name = "Матч тура по хоккею"
        verbose_name_plural = "Матчи тура по хоккею"
