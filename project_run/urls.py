from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from debug_toolbar.toolbar import debug_toolbar_urls

from .views import get_org_info, UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_run.urls')),
    path('api/', include(router.urls)),
    path('api/company_details/', get_org_info),
]

# Добавляем debug toolbar URL только для локальной разработки
urlpatterns.extend(debug_toolbar_urls())
