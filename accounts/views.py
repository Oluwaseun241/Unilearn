from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
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
    PasswordResetRequestSerializer)

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

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'No user with this email'}, status=status.HTTP_404_NOT_FOUND)

            # Generate the password reset token
            token = default_token_generator.make_token(user)

            # Send the password reset email
            reset_link = f'{settings.FRONTEND_URL}/reset-password?email={email}&token={token}'
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_link}',
                settings.EMAIL_FROM,
                [email],
                fail_silently=False,
            )

            return Response({'message': 'Password reset email sent'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)