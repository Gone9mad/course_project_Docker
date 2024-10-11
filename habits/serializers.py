from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import datetime

from habits.models import Habits, HabitLocation
from habits import validators

class HabitsSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[validators.DurationValidator], required=False)
    periodicity = serializers.IntegerField(validators=[validators.PeriodicityValidator], required=False)
    related = serializers.PrimaryKeyRelatedField(validators=[validators.RelatedHabitValidator()], required=False,
                                         queryset=Habits.objects.all())
    day = serializers.DateField(validators=[validators.DayValidator], required=False)

    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('related_habit', False) and attrs.get('reward', False):
            raise ValidationError('Невозможно заполнить поля "related_habit" и "reward" одновременно')

        if ((attrs.get('is_pleasant', False) is True and attrs.get('related_habit', False)) or
                (attrs.get('is_pleasant', False) is True and attrs.get('reward', False))):
            raise ValidationError('Приятная привычка не может иметь вознаграждение или связанной привычки.')

        if (attrs.get('day', datetime.utcnow().date()) == datetime.utcnow().date() and
                attrs.get('time') < datetime.utcnow().time()):
            raise ValidationError('Настоящее время не может быть прошлым')

        return attrs

class HabitLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HabitLocation
        fields = '__all__'
