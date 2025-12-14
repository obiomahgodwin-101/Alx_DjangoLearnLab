"""
URL configuration for advanced_api_project project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Connect api app URLs
    path('api/', include('api.urls')),
]

