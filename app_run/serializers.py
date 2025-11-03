from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Run


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class RunListSerializer(serializers.ModelSerializer):
    """Serializer for listing and retrieving runs with nested athlete data"""
    athlete_data = UserSerializer(source='athlete', read_only=True)

    class Meta:
        model = Run
        fields = ['id', 'athlete_data', 'comment', 'created_at']


class RunCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating runs"""

    class Meta:
        model = Run
        fields = '__all__'
