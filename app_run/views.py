from rest_framework import viewsets
from .models import Run
from .serializers import RunSerializer


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import AnonymousUser
from .models import Run
from .serializers import RunSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()
    serializer_class = RunSerializer
    permission_classes = [IsAuthenticated]  # Требуем аутентификацию для всех действий
    
    def perform_create(self, serializer):
        # Проверяем, что пользователь аутентифицирован
        if isinstance(self.request.user, AnonymousUser):
            raise ValueError("Аутентификация обязательна для создания записи")
        serializer.save(athlete=self.request.user)