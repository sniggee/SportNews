from rest_framework import serializers
from schedule.serializers import ScheduleSerializer


class TourMatchSerializer(serializers.Serializer):
    match = ScheduleSerializer()
    score = serializers.SerializerMethodField()

    def get_score(self, obj):
        return obj.score.split(":")


class TourSerializer(serializers.Serializer):
    tour = serializers.SerializerMethodField()
    matches = serializers.SerializerMethodField()

    def get_matches(self, obj):
        matches = [TourMatchSerializer(tour_match).data for tour_match in obj.matches.all()]

        return matches

    def get_tour(self, obj):
        return f"Тур {obj.num_of_tour}"
