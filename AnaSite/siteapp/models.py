from django.db import models

# Create your models here.

class Bilgisayar(models.Model):
    bilgisayarId = models.AutoField(primary_key=True)
    marka = models.CharField(max_length = 50)
    model = models.CharField(max_length = 50)
    ram = models.IntegerField()
    ssd = models.IntegerField()
    
    