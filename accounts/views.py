# Rest_framework Imports
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Own Imports
from .serializers import (
    UserSerializer,
    RegistrationSerializer,
    StudentSerializer,
    InstructorSerializer,
    ChangePasswordSerializer,
    UserProfileSerializer
)

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class ProfileUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        is_instructor = serializer.validated_data.get('is_instructor', False)
        if is_instructor:
            instructor_serializer = InstructorSerializer(data=request.data)
            instructor_serializer.is_valid(raise_exception=True)
            instructor = instructor_serializer.save(user=user)
            return Response(InstructorSerializer(instructor).data, status=status.HTTP_201_CREATED)
        else:
            student_serializer = StudentSerializer(data=request.data)
            student_serializer.is_valid(raise_exception=True)
            student = student_serializer.save(user=user)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
