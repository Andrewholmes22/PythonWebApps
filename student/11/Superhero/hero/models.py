from django.db import models
from django.urls import reverse_lazy
# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    strength = models.CharField(max_length=100,blank=True)
    weakness = models.CharField(max_length=100,blank=True)
    image = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('hero_list')