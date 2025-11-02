from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.conf import settings

from .serializers import UserSerializer

@api_view(['GET'])
def get_org_info(request):
    company_name = settings.COMPANY_NAME
    slogan = settings.SLOGAN
    contacts = settings.CONTACTS
    return Response(
        {
            'company_name': company_name,
            'slogan': slogan,
            'contacts':contacts,
        }
    )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # Исключаем суперпользователей
        queryset = self.queryset.exclude(is_superuser=True)
        
        # Получаем параметр type из query params
        user_type = self.request.query_params.get('type', None)
        
        if user_type == 'coach':
            # Возвращаем только тренеров (is_staff=True)
            queryset = queryset.filter(is_staff=True)
        elif user_type == 'athlete':
            # Возвращаем только атлетов (is_staff=False)
            queryset = queryset.filter(is_staff=False)
        # Если type не указан или имеет другое значение, возвращаем всех (кроме superuser)
        
        return queryset