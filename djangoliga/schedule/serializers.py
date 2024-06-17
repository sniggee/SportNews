from datetime import datetime

from rest_framework import serializers
from common.serializers import TeamSerilizer


class ScheduleSerializer(serializers.Serializer):
    first_team = TeamSerilizer()
    second_team = TeamSerilizer()
    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    is_ended = serializers.SerializerMethodField()

    def get_is_ended(self, obj) -> bool:
        combined_datetime = datetime.combine(obj.date, obj.time)
        current_datetime = datetime.now()

        return not combined_datetime > current_datetime

    def get_time(self, obj):
        return obj.time.strftime("%H:%M")

    def get_date(self, obj):
        return obj.date.strftime("%d.%m")


class ScheduleResponseSerizlizer(serializers.Serializer):
    date = serializers.SerializerMethodField()
    matches = serializers.SerializerMethodField()

    def get_date(self, obj):
        days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        months = [
            "января",
            "февраля",
            "марта",
            "апреля",
            "мая",
            "июня",
            "июля",
            "августа",
            "сентября",
            "октября",
            "ноября",
            "декабря",
        ]

        # Получаем день недели, день и месяц из поля DateTimeField
        day_of_week = obj["date"].strftime("%w")
        day = obj["date"].strftime("%d")
        month = obj["date"].strftime("%m")

        # Форматируем дату в нужный формат
        formatted_date = f"{days[int(day_of_week)-1]} {int(day)} {months[int(month)-1]}"

        return formatted_date

    def get_matches(self, obj):
        return ScheduleSerializer(obj["matches"], many=True).data
