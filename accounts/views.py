from django.shortcuts import render
# Rest_framework Imports
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
# Own Imports
from .models import User
from .serializers import UserSerializer

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
