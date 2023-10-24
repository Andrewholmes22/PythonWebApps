from django.views.generic import TemplateView
from pathlib import Path
from typing import Any
from django import http
from .models import Superhero




class IndexView(TemplateView):
    template_name = 'heroes.html'

class HeroView(TemplateView):
    template_name='hero.html'

    def get_context_data(self, **kwargs):
        id=kwargs['pk']
        hero= Superhero.objects.get(pk=id)
        image= f'static/images/{hero.image}'
        return {'hero':hero,'image':image}

class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        heroes=Superhero.objects.all()
        heroes=[f for f in heroes]
        return dict(heroes=heroes)