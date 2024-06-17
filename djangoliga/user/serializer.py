from rest_framework import serializers
from .models import Subs_info


class SubsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subs_info
        fields = '__all__'
