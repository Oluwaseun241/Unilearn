from django.shortcuts import render
# Rest_framework Imports
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
# Own Imports
from .models import User
from .serializers import (
    UserSerializer, 
    UserRegisterSerializer, 
    StudentSerializer, 
    InstructorSerializer,
    ChangePasswordSerializer
    )

class RegisterUserView(generics.CreateAPIView):
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

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self,queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args,**kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # Set new password
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)