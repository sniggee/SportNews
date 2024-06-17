from django.contrib import admin

from .models import ScheduleBassketball, ScheduleFootball, ScheduleHockey

admin.site.register(ScheduleBassketball)
admin.site.register(ScheduleFootball)
admin.site.register(ScheduleHockey)
