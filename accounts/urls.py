from django.urls import path
# Own imports
from .views import RegisterUser

urlpatterns = [
    path("register/", RegisterUser.as_view(), name='user-register'),
    # path("login/"),
]
