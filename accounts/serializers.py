# Rest_framework imports
from rest_framework import serializers
# Own imports
from .models import User, Instructor, Student


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'is_instructor']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    is_instructor = serializers.BooleanField(default=False)
    matric_no = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        user_id = self.context['user_id']

        is_instructor = validated_data.get('is_instructor', False)
        if is_instructor:
            instructor = Instructor.objects.create(user_id=user_id, **validated_data)
            return instructor
        else:
            student = Student.objects.create(user_id=user_id, **validated_data)
            return student

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
