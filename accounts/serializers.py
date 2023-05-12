# Rest_framework imports
from rest_framework import serializers
# Own imports
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name', 'is_instructor')
        extra_kwargs = {'id': {'read_only': True}, 'is_instructor': {'read_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_instructor')
        extra_kwargs = {'id': {'read_only': True}}