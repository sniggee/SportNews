from rest_framework import serializers

from .models import Info, Subs_info, Comment


class SubsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subs_info
        fields = "__all__"


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class DateMixinSerializer(serializers.Serializer):
    date = serializers.SerializerMethodField()
    
    def get_data(self, obj):
        return obj.data.strftime("%Y.%m.%d")

class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.CharField()
    data = serializers.SerializerMethodField()
    
    def get_data(self, obj):
        return obj.data.strftime("%Y.%m.%d")

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ["user", "news", "text", "date"]
    
    def get_user(self, obj):
        return obj.user.username
    
    def get_date(self, obj):
        return obj.date.strftime("%Y.%m.%d")