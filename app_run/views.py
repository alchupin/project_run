from rest_framework import viewsets
from .models import Run
from .serializers import RunSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()
    serializer_class = RunSerializer
    
    def perform_create(self, serializer):
        serializer.save(athlete=self.request.user)