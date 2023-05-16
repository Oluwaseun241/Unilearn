from django.shortcuts import render
# Rest_framework Imports
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
# Own Imports
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer, StudentSerializer, InstructorSerializer

class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = None

    def get_serializer_class(self):
        if self.serializer_class is None:
            is_instructor = self.request.data.get('is_instructor', False)
            if is_instructor:
                self.serializer_class = InstructorSerializer
            else:
                self.serializer_class = StudentSerializer
        return self.serializer_class
