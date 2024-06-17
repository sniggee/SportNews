import json

from django.http import HttpResponse
from django.views.generic import View

from .models import ScheduleBassketball, ScheduleFootball, ScheduleHockey
from .serializers import ScheduleResponseSerizlizer
from .sort_matches_by_date import sort_matches_by_date


class GetScheduleBasketball(View):
    def get(self, request):
        matches = ScheduleBassketball.objects.all()
        response = sort_matches_by_date(matches)

        return HttpResponse(json.dumps(ScheduleResponseSerizlizer(response, many=True).data))


class GetScheduleHockey(View):
    def get(self, request):
        matches = ScheduleHockey.objects.all()
        response = sort_matches_by_date(matches)

        return HttpResponse(json.dumps(ScheduleResponseSerizlizer(response, many=True).data))


class GetScheduleFootball(View):
    def get(self, request):
        matches = ScheduleFootball.objects.all()
        response = sort_matches_by_date(matches)

        return HttpResponse(json.dumps(ScheduleResponseSerizlizer(response, many=True).data))
