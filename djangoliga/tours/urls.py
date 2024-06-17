from django.urls import path
from .views import GetFootballTours, GetBasketballTours, GetHockeyTours


urlpatterns = [
    path('football', GetFootballTours.as_view()),
    path('basketball', GetBasketballTours.as_view()),
    path('hockey', GetHockeyTours.as_view())
]