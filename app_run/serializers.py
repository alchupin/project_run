from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Run


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class RunSerializer(serializers.ModelSerializer):
    athlete = UserSerializer(read_only=True)
    class Meta:
        model = Run
        fields = '__all__'
