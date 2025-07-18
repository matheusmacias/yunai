from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
