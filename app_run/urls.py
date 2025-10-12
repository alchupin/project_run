from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RunViewSet


router = DefaultRouter()
router.register('runs', RunViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
