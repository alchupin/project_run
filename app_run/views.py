from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Run
from .serializers import RunListSerializer, RunCreateSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()

    def get_serializer_class(self):
        """Return appropriate serializer class based on action"""
        if self.action in ['list', 'retrieve']:
            return RunListSerializer
        return RunCreateSerializer

    def create(self, request, *args, **kwargs):
        """Create a new run and return it with athlete_data"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Use RunListSerializer to return the created object with athlete_data
        instance = serializer.instance
        output_serializer = RunListSerializer(instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)