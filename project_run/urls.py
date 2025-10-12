from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import get_org_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_run.urls')),
    path('api/company_details/', get_org_info),
]