from django.urls import path
from .views import *


urlpatterns = [
    path('save_matches/', save_matches_view),
    path('manual/match/', Manualinfo.as_view()),
    path('manual/match/<int:pk>/', Manualinfo_get_post_path.as_view()),
    path('match/', MatchAPIView.as_view()),
    path('football', GetFootballTable.as_view()),
    path('basketball', GetBasketballTable.as_view()),
    path('hockey', GetHockeyTable.as_view()),
]
