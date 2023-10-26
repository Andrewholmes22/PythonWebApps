from django.urls import path, include
from django.contrib import admin
from hero.views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView,HeroView
from django.contrib.admin import site

# urlpatterns = [
#     path(r'admin/',site.urls),
#     path('', HeroListView.as_view()),
#     path('hero/<int:pk>', HeroView.as_view()),
# ]


urlpatterns = [

    # Hero
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    path(r'admin/',site.urls),
    path('hero/<int:pk>', HeroView.as_view()),
    # Login/Logout code
    

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
