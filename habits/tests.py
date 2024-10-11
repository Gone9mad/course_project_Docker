from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits, HabitLocation
from users.models import User


class HabitLocationTestCase(APITestCase):
    maxDiff = None

    def setUp(self):
        '''
            Cпециальный метод для установки
            взаимодействия с данными для теста, например для заполнения первичных данныx.
        '''

        self.user = User.objects.create(email='test@test.ru', password='1234', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        response = self.client.post(
            reverse('habits:habit-location-create'),
            data={'location': 'test'}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                          {
                              'id': HabitLocation.objects.last().pk,
                              'location': 'test'
                          }
                          )


class HabitsTestCase(APITestCase):
    maxDiff = None


    def setUp(self):
        '''
            Cпециальный метод для установки
            взаимодействия с данными для теста, например для заполнения первичных данныx.
        '''

        self.user = User.objects.create(email='test@test.ru', password='1234', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.location = HabitLocation.objects.create(location='test')

        self.first_habit = Habits.objects.create(owner=self.user, location=self.location, time='15:00',
                                                 action='test-action-1', periodicity=1, reward='test-reward-1',
                                                 duration=50, is_pleasant=False, is_publicity=True)

        self.second_habit = Habits.objects.create(owner=self.user, location=self.location, time='16:00',
                                                  action='test-action-2', periodicity=2, reward='test-reward-2',
                                                  duration=60, is_pleasant=False, is_publicity=True)

    def test_list_habit(self):
        '''
            Метод-тест, название которого должно
            начинаться со специального слова test_, так гарантируется запуск метода как теста.
        '''

        response = self.client.get(
            reverse('habits:habits-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.first_habit.pk,
                    'owner': self.first_habit.owner.pk,
                    'location': self.first_habit.location.pk,
                    'time': '15:00:00',
                    'action': self.first_habit.action,
                    'related_habit': self.first_habit.related_habit,
                    'periodicity': self.first_habit.periodicity,
                    'reward': self.first_habit.reward,
                    'duration': self.first_habit.duration,
                    'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                    'is_pleasant': self.first_habit.is_pleasant,
                    'is_publicity': self.first_habit.is_publicity
                },
                {
                    'id': self.second_habit.pk,
                    'owner': self.second_habit.owner.pk,
                    'location': self.second_habit.location.pk,
                    'time': '16:00:00',
                    'action': self.second_habit.action,
                    'related_habit': self.second_habit.related_habit,
                    'periodicity': self.second_habit.periodicity,
                    'reward': self.second_habit.reward,
                    'duration': self.second_habit.duration,
                    'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                    'is_pleasant': self.second_habit.is_pleasant,
                    'is_publicity': self.second_habit.is_publicity
                }
            ]
        })

    def test_list_public_habit(self):
        response = self.client.get(
            reverse('habits:public-list')
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {
            'count': 2,
            'next': None,
            'previous': None,
            'results': [
                {
                    'id': self.first_habit.pk,
                    'owner': self.first_habit.owner.pk,
                    'location': self.first_habit.location.pk,
                    'time': '15:00:00',
                    'action': self.first_habit.action,
                    'related_habit': self.first_habit.related_habit,
                    'periodicity': self.first_habit.periodicity,
                    'reward': self.first_habit.reward,
                    'duration': self.first_habit.duration,
                    'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                    'is_pleasant': self.first_habit.is_pleasant,
                    'is_publicity': self.first_habit.is_publicity
                },
                {
                    'id': self.second_habit.pk,
                    'owner': self.second_habit.owner.pk,
                    'location': self.second_habit.location.pk,
                    'time': '16:00:00',
                    'action': self.second_habit.action,
                    'related_habit': self.second_habit.related_habit,
                    'periodicity': self.second_habit.periodicity,
                    'reward': self.second_habit.reward,
                    'duration': self.second_habit.duration,
                    'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                    'is_pleasant': self.second_habit.is_pleasant,
                    'is_publicity': self.second_habit.is_publicity
                }
            ]
        })

    def test_update(self):
        response = self.client.patch(
            reverse('habits:habits-update', args=[self.first_habit.pk]),
            data={'time': '17:00:00'}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {
                             'id': self.first_habit.pk,
                             'owner': self.user.pk,
                             'location': self.location.pk,
                             'time': '17:00:00',
                             'action': 'test-action-1',
                             'related_habit': None,
                             'periodicity': 1,
                             'reward': 'test-reward-1',
                             'duration': 50,
                             'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                             'is_pleasant': False,
                             'is_publicity': True
                         }
                         )




    def test_delete(self):
        response = self.client.delete(
            reverse('habits:habits-destroy', args=[self.first_habit.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


"""
                          
        def test_create(self):
        response = self.client.post(
            reverse('habits:habits-create'),
            data={'time': '16:00:00', 'action': 'test', 'periodicity': 1, 'reward': 'test',
                  'duration': 70, 'is_pleasant': False, 'is_publicity': True}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                          {
                              'id': Habits.objects.last().pk,
                              'owner': self.user.pk,
                              'location': self.location.pk,
                              'time': '16:00:00',
                              'action': "test",
                              'related_habit': None,
                              'periodicity': 1,
                              'reward': 'test',
                              'duration': 70,
                              'day': datetime.utcnow().date().strftime("%Y-%m-%d"),
                              'is_pleasant': False,
                              'is_publicity': True
                          }
                          )
"""
