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
    
    HepsiBuradaPrice = models.CharField(max_length = 300, blank=True)
    HepsiBuradaURL = models.CharField(max_length = 300, blank=True)
    HepsiBuradaRating = models.CharField(max_length = 300, blank=True)

    teknosaPrice = models.CharField(max_length = 300, blank=True)
    teknosaURL = models.CharField(max_length = 300, blank=True)
    teknosaRating = models.CharField(max_length = 300, blank=True)

    AmazonPrice= models.CharField(max_length = 300, blank=True)
    AmazonURL = models.CharField(max_length = 300, blank=True)
    AmazonRating = models.CharField(max_length = 300, blank=True)

    vatanBilgisayarPrice = models.CharField(max_length = 300, blank=True)
    vatanBilgisayarURL= models.CharField(max_length = 300, blank=True)
    vatanBilgisayarRating = models.CharField(max_length = 300, blank=True)

    cicekSepetiExtraPrice = models.CharField(max_length = 300, blank=True)
    cicekSepetiExtraURL = models.CharField(max_length = 300, blank=True)
    cicekSepetiExtraRating = models.CharField(max_length = 300, blank=True)

    TrendyolPrice = models.CharField(max_length = 300, blank=True)
    TrendyolURL= models.CharField(max_length = 300, blank=True)
    TrendyolRating = models.CharField(max_length = 300, blank=True)

    n11Price = models.CharField(max_length = 300, blank=True)
    n11URL = models.CharField(max_length = 300, blank=True)
    n11Rating= models.CharField(max_length = 300, blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.marka}"