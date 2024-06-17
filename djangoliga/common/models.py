from django.db import models


class Team(models.Model):
    name = models.CharField(verbose_name=u"Название комманды", max_length=50)
    image = models.URLField(verbose_name=u"Лого комманды", null=True, blank=True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

        
class FootballTeam(Team):
    class Meta:
        verbose_name = u"Футбольная комманда"
        verbose_name_plural = u"Футбольные комманды"

class BasketballTeam(Team):
    class Meta:
        verbose_name = u"Баскетбольная комманда"
        verbose_name_plural = u"Баскетбольные комманды"
        
class HockeyTeam(Team):
    class Meta:
        verbose_name = u"Хоккейная комманда"
        verbose_name_plural = u"Хоккейные комманды"

class Sport(models.Model):
    name = models.CharField(verbose_name=u"Название спорта", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u"Спорт"
        verbose_name_plural = u"Виды спорта"