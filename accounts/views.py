from django.shortcuts import render
# Rest_framework Imports
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
# Own Imports
from .models import User, Student
from .serializers import (
    RegisterUserSerializer,
    StudentSerializer,
    InstructorSerializer,
    ChangePasswordSerializer
)


class RegisterUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        is_instructor = request.data.get('is_instructor', False)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if is_instructor:
            instructor_serializer = InstructorSerializer(data=request.data)
            instructor_serializer.is_valid(raise_exception=True)
            instructor = instructor_serializer.save()
            user = User.objects.create_user(email=serializer.validated_data['email'],
                                            password=serializer.validated_data['password'],
                                            name=serializer.validated_data['name'],
                                            is_instructor=True)
            instructor.user = user
            instructor.save()
        else:
            user = User.objects.create_user(email=serializer.validated_data['email'],
                                            password=serializer.validated_data['password'],
                                            name=serializer.validated_data['name'],
                                            is_instructor=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
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
