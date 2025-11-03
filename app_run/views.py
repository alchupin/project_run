from rest_framework import viewsets
from .models import Run
from .serializers import RunListSerializer, RunCreateSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()

    def get_serializer_class(self):
        """Return appropriate serializer class based on action"""
        if self.action in ['list', 'retrieve']:
            return RunListSerializer
        return RunCreateSerializer