from rest_framework.permissions import AllowAny
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import (UserCreateAPIView, UserUpdateAPIView, UserDetailAPIView,
                         UserDeleteAPIView, UserListAPIView)
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(permission_classes=(AllowAny, )), name='register'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny, )), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny, )), name='token_refresh'),
]