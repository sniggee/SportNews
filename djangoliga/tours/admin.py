from django.contrib import admin

from .models import (
    BasketballTour,
    BasketballTourMatch,
    FootballTour,
    FootballTourMatch,
    HockeyTour,
    HockeyTourMatch,
)

admin.site.register(FootballTourMatch)
admin.site.register(BasketballTourMatch)
admin.site.register(HockeyTourMatch)
admin.site.register(HockeyTour)
admin.site.register(FootballTour)
admin.site.register(BasketballTour)
