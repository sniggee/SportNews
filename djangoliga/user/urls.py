from django.urls import path
from .views import Register, Login, Logout, Profile
from .views import change_password, Subs_post, Subs_get_post_delete


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('profile/', Profile.as_view()),
    path('subs/', Subs_post.as_view()),
    path('subs/<int:pk>/', Subs_get_post_delete.as_view()),
    path('change_password/', change_password),
]
