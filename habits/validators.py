'''
    Валидаторы (validators) в Django REST framework — инструмент, который проверяет данные,
    полученные от клиента, и убеждается в их правильности перед сохранением или использованием в приложении.
    Валидаторы позволяют установить правила и ограничения для полей сериализаторов и предоставить обратную связь
    пользователю в случае ошибок валидации.
'''

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
