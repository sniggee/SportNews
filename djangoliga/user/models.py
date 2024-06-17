from django.db import models


class Subs_info(models.Model):
    title = models.CharField("Название команды  ", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "подписки юзеров"
        verbose_name_plural = "подписки юзеров"
