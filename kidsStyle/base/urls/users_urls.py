from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from base.views.user_views import RegisterUser, UserProfileUpdateView, UpdatePasswordView, UserProfileView


urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterUser.as_view(), name='register'),
    path('me', UserProfileView.as_view(), name='me'),
    path('update-details', UserProfileUpdateView.as_view(), name='updateDetails'),
    path('update-password', UpdatePasswordView.as_view(), name='updatePassword'),
]
