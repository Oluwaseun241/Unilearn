# Rest_framework imports
from rest_framework import serializers
from django.core.exceptions import ValidationError
# Own imports
from .models import User, Instructor, Student


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'email', 'password', 'name', 'is_instructor']
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exist")
        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.message)
        return value


    # Create new user
    def create(self, validated_data):
        user = User.objects.create_user(
            email= validated_data['email'],
            name= validated_data['name'],
            password=validated_data['password'],
            is_instructor=validated_data['is_instructor']
            )
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'created_at', 'is_instructor', 'created_at']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        fields = '__all__'
