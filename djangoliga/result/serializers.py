from rest_framework import serializers
from common.serializers import TeamSerilizer

from .models import ManualMatch, Match


class ManualSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManualMatch
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"


class ResultSerilizer(serializers.Serializer):
    team = TeamSerilizer()
    matches = serializers.CharField()
    wins = serializers.CharField()
    draws = serializers.CharField()
    losses = serializers.CharField()
    goalsFor = serializers.CharField()
    goalsAgainst = serializers.CharField()
    goalDifference = serializers.CharField()
    points = serializers.CharField()


class BasketballResultsSerilizer(serializers.Serializer):
    team = TeamSerilizer()
    matches = serializers.CharField()
    goalsFor = serializers.CharField()
    goalsMissed = serializers.CharField()
    wins = serializers.CharField()
    looses = serializers.CharField()
    total_points = serializers.CharField()


class HockeyResultsSerilizer(serializers.Serializer):
    team = TeamSerilizer()
    matches = serializers.CharField()
    goalsFor = serializers.CharField()
    points = serializers.CharField()
    wins = serializers.CharField()
    goalsMissed = serializers.CharField()
    looses = serializers.CharField()
    
