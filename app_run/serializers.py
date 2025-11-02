from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Run


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

from django.contrib.auth.models import AnonymousUser

class RunSerializer(serializers.ModelSerializer):
    athlete = UserSerializer(read_only=True)
    class Meta:
        model = Run
        fields = '__all__'
    
    def create(self, validated_data):
        # Если athlete не передан, используем текущего пользователя
        request = self.context.get('request', None)
        if 'athlete' not in validated_data and request and hasattr(request, 'user'):
            if isinstance(request.user, AnonymousUser):
                raise serializers.ValidationError("Аутентификация обязательна для создания записи")
            validated_data['athlete'] = request.user
        return super().create(validated_data)
