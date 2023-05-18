from django.urls import path, include
# Own imports
from .views import RegisterUserView, ChangePasswordView, ProfileUserView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterUserView.as_view(), name='register_user'),
    path("user-profile/", ProfileUserView.as_view(), name='user_profile'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("login/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("change-password/", ChangePasswordView.as_view(), name='change_password'),
    path("reset-password/", include('django_rest_passwordreset.urls', namespace='password_reset'))
]
