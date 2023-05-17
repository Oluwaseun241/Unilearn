from django.urls import path, include
# Own imports
from .views import RegisterUser, PasswordResetRequestView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterUser.as_view(), name='register_user'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("login/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("reset-password/", PasswordResetRequestView.as_view(), name='reset_passwoord')
]
