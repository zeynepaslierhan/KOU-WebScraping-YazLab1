from dataclasses import field
from enum import unique
from django.db import models
from djongo import models
import pymongo

# Create your models here.

class Ürünler(models.Model):
    name = models.CharField(max_length= 200)
    id = models.AutoField(primary_key=True)
    index = models.IntegerField()
    
    image = models.CharField(max_length = 300)
    marka = models.CharField(max_length = 100, blank=True)
    ağırlık = models.CharField(max_length = 20, blank=True)
    renk = models.CharField(max_length = 20, blank=True)
    ram = models.CharField(max_length = 20, blank=True)
    bellek_hızı = models.CharField(max_length = 20, blank=True)
    ekran_kartı = models.CharField(max_length = 50, blank=True)
    işlemci = models.CharField(max_length = 50, blank=True)
    dos = models.CharField(max_length = 50, blank=True)
    
    hepsiburadaFiyat = models.FloatField()
    hepsiburadaUrl = models.CharField(max_length = 300)
    hepsiburadaRating = models.FloatField(blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.marka}"