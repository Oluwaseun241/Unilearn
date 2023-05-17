from django.shortcuts import render
from rest_framework.response import Response
# Rest_framework Imports
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
# Own Imports
from .models import User
from .serializers import UserSerializer, UserRegisterSerializer, StudentSerializer, InstructorSerializer

class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = None

    def post(self, request):
        email = request.data.get('email', None)
        if email is not None:
            if Student.objects.filter(email=email).exist():
                return Response({'message': 'User is already registered as a student.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.serializer_class is None:
            is_instructor = self.request.data.get('is_instructor', False)
            if is_instructor:
                self.serializer_class = InstructorSerializer
            else:
                self.serializer_class = StudentSerializer
        return self.serializer_class
