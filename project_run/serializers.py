from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'date_joined', 'username', 'last_name', 'first_name', 'type']

    def get_type(self, obj):
        """Определяет тип пользователя на основе поля is_staff"""
        if obj.is_staff:
            return 'coach'
        return 'athlete'