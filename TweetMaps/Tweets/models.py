from django.db import models

# Create your models here.

class Tweet(models.Model):
    titulo = models.CharField(max_length=10,default='Titulo')
