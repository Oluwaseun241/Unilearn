from django.urls import path
# Own imports
from .views import RegisterUser
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterUser.as_view(), name='register-user'),
    path("login/", TokenObtainPairView.as_view(), name='login'),
    path("login/refresh", TokenRefreshView.as_view(), name='token-refresh')
]
