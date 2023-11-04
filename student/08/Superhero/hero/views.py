from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,DetailView,ListView
from pathlib import Path
from typing import Any
from django import http
from .models import Superhero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from.models import Superhero


class IndexView(TemplateView):
    template_name = 'heroes.html'

class HeroView(TemplateView):
    template_name='hero.html'

    def get_context_data(self, **kwargs):
        id=kwargs['pk']
        hero= Superhero.objects.get(pk=id)
        image= f'/static/images/{hero.image}'
        return {'hero':hero,'image':image}

class HeroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        heroes=Superhero.objects.all()
        heroes=[f for f in heroes]
        return dict(heroes=heroes)


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')