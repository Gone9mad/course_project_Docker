from datetime import date

from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class HabitLocation(models.Model):
    location = models.CharField(max_length=150, unique=True, verbose_name="Место положение")

    class Meta:
        verbose_name = 'Место положение'
        verbose_name_plural = 'Места положения'

    def __str__(self):
        return f'{self.location}'


class Habits(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE,
                              **NULLABLE)
    location = models.ForeignKey(HabitLocation, verbose_name='Место положение', on_delete=models.SET_DEFAULT, default=1)
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=300, verbose_name='Действие')
    related_habit = models.ForeignKey('Habits', verbose_name='Связанная привычка', on_delete=models.SET_NULL,
                                      **NULLABLE)
    periodicity = models.PositiveIntegerField(verbose_name='Переодичность', default=1)
    reward = models.CharField(max_length=300, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.PositiveIntegerField(verbose_name='Время на выполнение')
    day = models.DateField(verbose_name='День выполнения', default=date.today)

    is_pleasant = models.BooleanField(verbose_name='Приятная привычка')
    is_publicity = models.BooleanField(default=False, verbose_name='Опубликованна')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.location}'
