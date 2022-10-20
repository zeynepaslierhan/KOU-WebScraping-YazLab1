from django.db import models


# Create your models here.

class Bilg(models.Model):
    pcId = models.AutoField(primary_key=True)
    isim = models.CharField(max_length = 200)
    fiyat1 = models.FloatField()
    fiyat2 = models.FloatField()
    fiyat3 = models.FloatField()
    image = models.ImageField(upload_to = 'static/pc_img')
    
    