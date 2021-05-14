from django.db import models
# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=150,default='Titulo')
    posted = models.DateTimeField()
    titulo = models.TextField(default='default message')
    latitud = models.FloatField()
    longitud = models.FloatField()
    user = models.CharField(max_length=150,default='usuario')
    url = models.URLField(max_length=200,default='url/gsj')
    location = models.CharField(max_length=150,default='paisciudad')
    language = models.CharField(max_length=150,default='idioma')
    num_retweets = models.IntegerField(default=0)
    source = models.CharField(max_length=150,default='Android')