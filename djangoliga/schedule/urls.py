from django.urls import path
from .views import GetScheduleBasketball, GetScheduleHockey, GetScheduleFootball


urlpatterns = [
    path('schedule/basketball', GetScheduleBasketball.as_view()),
    path('schedule/hockey', GetScheduleHockey.as_view()),
    path('schedule/football', GetScheduleFootball.as_view())
]