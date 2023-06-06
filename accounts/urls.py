from django.urls import path, include
# Own imports
from .views import (
    RegisterUserView,
    ChangePasswordView,
    ProfileUserView,
    UserProfileUpdateView
)
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterUserView.as_view(), name='register_user'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("login/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("login/verify", TokenVerifyView.as_view(), name='token_verify'),
    path("logout/", TokenBlacklistView.as_view(), name='token_blacklist'),
    path("change-password/", ChangePasswordView.as_view(), name='change_password'),
    path("reset-password/", include('django_rest_passwordreset.urls', namespace='password_reset')),
    # User profile
    path("user-profile/", ProfileUserView.as_view(), name='user_profile'),
    path("profile/update", UserProfileUpdateView.as_view(), name='profile-update'),
    path("", include("course.urls"))
]
