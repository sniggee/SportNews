from django.contrib import admin
from .models import FootballTeam, BasketballTeam, HockeyTeam, Sport


admin.site.register(FootballTeam)
admin.site.register(BasketballTeam)
admin.site.register(HockeyTeam)
admin.site.register(Sport)
