from django.urls import path
from django.contrib import admin
from hero.views import HeroListView, HeroView
from django.contrib.admin import site

urlpatterns = [
    path(r'admin/',site.urls),
    path('', HeroListView.as_view()),
    path('hero/<int:pk>', HeroView.as_view()),
]