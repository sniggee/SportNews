from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('user/', include('user.urls')),
    path('result/', include('result.urls')),
    path('auto/', include('autonews.urls')),
    path('schedule/', include('schedule.urls')),
    path('tours/', include('tours.urls'))
]
