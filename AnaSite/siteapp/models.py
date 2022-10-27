from dataclasses import field
from enum import unique
from django.db import models
from djongo import models
import pymongo

# Create your models here.

class Ürün(models.Model):
    
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length= 200)
    index = models.IntegerField()
    Img = models.CharField(max_length = 300)

    Marka = models.CharField(max_length = 100, blank=True)
    BellekHızı = models.CharField(max_length = 20, blank=True)
    HDMI = models.CharField(max_length = 20, blank=True)
    EkranKartıBellekTipi = models.CharField(max_length = 20, blank=True)
    Renk = models.CharField(max_length = 20, blank=True)
    RamTipi = models.CharField(max_length = 50, blank=True)
    
    HepsiBuradaPrice = models.FloatField()
    HepsiBuradaURL = models.CharField(max_length = 300)
    HepsiBuradaRating = models.FloatField(blank=True)

    teknosaPrice = models.FloatField()
    teknosaURL = models.CharField(max_length = 300)
    teknosaRating = models.FloatField(blank=True)

    AmazonPrice = models.FloatField()
    AmazonURL = models.CharField(max_length = 300)
    AmazonRating = models.FloatField(blank=True)

    vatanBilgisayarPrice = models.FloatField()
    vatanBilgisayarURL = models.CharField(max_length = 300)
    vatanBilgisayarRating = models.FloatField(blank=True)

    cicekSepetiExtraPrice = models.FloatField()
    cicekSepetiExtraURL = models.CharField(max_length = 300)
    cicekSepetiExtraRating = models.FloatField(blank=True)

    TrendyolPrice = models.FloatField()
    TrendyolURL = models.CharField(max_length = 300)
    TrendyolRating = models.FloatField(blank=True)

    n11Price = models.FloatField()
    n11URL = models.CharField(max_length = 300)
    n11Rating = models.FloatField(blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.marka}"