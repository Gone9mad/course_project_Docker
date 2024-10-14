from datetime import date

from rest_framework.exceptions import ValidationError


class DurationValidator:

    def __call__(self, value):
        if value > 120:
            raise ValidationError('Duration should not exceed 120 secund.')


class PeriodicityValidator:

    def __call__(self, value):
        if value > 7:
            raise ValidationError('Periodicity should not exceed 7 days.')


class RelatedHabitValidator:

    def __call__(self, value):
        if not value.is_pleasant:
            raise ValidationError('Related habit should be pleasant.')


class DayValidator:

    def __call__(self, value):
        if value < date.today():
            raise ValidationError('Day should not be in the past.')
