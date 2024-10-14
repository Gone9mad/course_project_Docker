from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits, HabitLocation
from habits.paginators import HabitsPagination
from habits.serializers import HabitLocationSerializers, HabitsSerializer
from users.permissions import IsOwner


class HabitsPublicListView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_publicity=True)
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitsPagination


class HabitsListView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitsPagination

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitsCreateView(generics.CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitsUpdateView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitLocationCreateView(generics.CreateAPIView):
    queryset = HabitLocation.objects.all()
    serializer_class = HabitLocationSerializers
    permission_classes = [IsAuthenticated]
