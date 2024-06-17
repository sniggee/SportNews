from django.contrib import admin

from .models import BasketballResult, FootbalResult, HockeyResult, ManualMatch, Match

admin.site.register(Match)
admin.site.register(ManualMatch)
admin.site.register(FootbalResult)
admin.site.register(BasketballResult)
admin.site.register(HockeyResult)
