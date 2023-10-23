from django.contrib.admin import site
from django.urls import path
from django.urls.conf import include
from django.contrib import admin

urlpatterns = [
    path(r'admin/', site.urls),
]
