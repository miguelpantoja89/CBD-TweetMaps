from django.db import models
# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=10,default='Titulo')
    created_at = models.DateTimeField(auto_now=True)
    titulo = models.TextField(default='hola chao chao')
    latitud = models.FloatField()
    longitud = models.FloatField()
