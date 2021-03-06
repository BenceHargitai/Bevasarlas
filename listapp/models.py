from django.db import models

# Create your models here.

class Lista(models.Model):
    nev = models.CharField(max_length=50)
    mennyiseg = models.CharField(max_length=20)