from django.urls import path

from habits.views import (HabitsListView, HabitsCreateView, HabitsUpdateView,
                          HabitsDestroyView, HabitsPublicListView, HabitLocationCreateView)

urlpatterns = [
    path('', HabitsPublicListView.as_view(), name='public-list'),
    path('list/', HabitsListView.as_view(), name='habits-list'),
    path('create/', HabitsCreateView.as_view(), name='habits-create'),
    path('destroy/<int:pk>/', HabitsDestroyView.as_view(), name='habits-destroy'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(), name='habits-update'),
    path('location_create/', HabitLocationCreateView.as_view(), name='habit-location-create'),
]