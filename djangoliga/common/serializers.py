from rest_framework import serializers


class TeamSerilizer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.CharField()