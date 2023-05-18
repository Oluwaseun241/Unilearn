# Rest_framework imports
from rest_framework import serializers
from django.core.exceptions import ValidationError
# Own imports
from .models import User, Instructor, Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'is_instructor']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    user = user = user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_student(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

class InstructorSerializer(serializers.ModelSerializer):
    user = user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Instructor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_instructor(**user_data)
        instructor = Instructor.objects.create(user=user, **validated_data)
        return instructor

class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    is_instructor = serializers.BooleanField(default=False)
    matric_no = serializers.IntegerField(required=False)

    def create(self, validated_data):
        # This method is called when creating the user

        # Remove the `is_instructor` flag from the validated data
        is_instructor = validated_data.pop('is_instructor', False)

        # Create the user instance
        user = User.objects.create_user(**validated_data)

        # Check if the user is an instructor or student
        if is_instructor:
            Instructor.objects.create(user=user)
        else:
            Student.objects.create(user=user)

        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
