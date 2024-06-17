from django.db import models
from common.models import Sport
from django.contrib.auth.models import User


class Info(models.Model):
    sport = models.ForeignKey(Sport, verbose_name=u"Вид спорта", on_delete=models.SET_NULL, null=True)
    title = models.CharField("Название новостей  ", max_length=70)
    description = models.TextField("Описание")
    photo = models.CharField("Ссылка на фото", max_length=1000)
    data = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"

class Subs_info(models.Model):
    title = models.CharField("Название комманды  ", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "подписки юзеров"
        verbose_name_plural = "подписки юзеров"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    news = models.ForeignKey(Info, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)