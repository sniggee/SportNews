from django.urls import path

from .views import (
    Info_get_post_path,
    Info_get_post_path_Basket,
    Info_get_post_path_Hokey,
    Infopost,
    Infopost_Basket,
    Infopost_Hokey,
    GetComments,
    CreateComment
)

urlpatterns = [
    path("info/<int:pk>/", Info_get_post_path.as_view()),
    path("info/", Infopost.as_view()),
    path("basket/info/<int:pk>/", Info_get_post_path_Basket.as_view()),
    path("basket/info/", Infopost_Basket.as_view()),
    path("hokey/info/<int:pk>/", Info_get_post_path_Hokey.as_view()),
    path("hokey/info/", Infopost_Hokey.as_view()),
    path("comments/<int:news_id>", GetComments.as_view()),
    path("comment", CreateComment.as_view())
]
