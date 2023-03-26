from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomUserRegister, UserLogin, UserProfileView, ChangePasswordView

urlpatterns = [
    path('current/', UserProfileView.as_view()),
    path('register/', CustomUserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogin.as_view(), name='user-logout'),
    path('password', ChangePasswordView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
