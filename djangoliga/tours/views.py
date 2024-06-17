import json

from django.http import HttpResponse
from django.views.generic import View

from .models import BasketballTour, FootballTour, HockeyTour
from .serializers import TourSerializer


class GetFootballTours(View):
    def get(self, request):
        tours = FootballTour.objects.prefetch_related("matches").all()

        return HttpResponse(json.dumps(TourSerializer(tours, many=True).data))


class GetBasketballTours(View):
    def get(self, request):
        tours = BasketballTour.objects.prefetch_related("matches").all()

        return HttpResponse(json.dumps(TourSerializer(tours, many=True).data))


class GetHockeyTours(View):
    def get(self, request):
        tours = HockeyTour.objects.prefetch_related("matches").all()

        return HttpResponse(json.dumps(TourSerializer(tours, many=True).data))
