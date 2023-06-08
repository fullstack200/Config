from django.db import models
from django.urls import reverse
# Create your models here.

class Laptop(models.Model):
    typ = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    weight = models.FloatField()
    size = models.FloatField()
    color =  models.CharField(max_length=50)
    processorBrand = models.CharField(max_length=50)
    processorModel = models.CharField(max_length=50)
    ram = models.IntegerField()
    storageType = models.CharField(max_length= 10)
    storageMemory=models.CharField(max_length=50)
    batteryLife = models.IntegerField()
    graphicsCardBrand = models.CharField(max_length=50)
    graphicsCardModel = models.CharField(max_length=50)
    graphicsMemory = models.IntegerField()
    screenQuality = models.TextField()
    os = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    extraInfo = models.TextField()
    pros = models.TextField()
    cons = models.TextField()
    amazonLink = models.URLField()
    flipkartLink = models.URLField()
    img1 = models.ImageField(null = True, blank = True, upload_to="upload/")
    img2 = models.ImageField(null = True, blank = True,upload_to="upload/")
    img3 = models.ImageField(null = True, blank = True,upload_to="upload/")
    img4 = models.ImageField(null = True, blank = True,upload_to="upload/")
    img5 = models.ImageField(null = True, blank = True,upload_to="upload/")
    img6 = models.ImageField(null = True, blank = True,upload_to="upload/")

    def __str__(self):
        return self.brand

    def splitx(self):
        if self.extraInfo:
            return self.extraInfo.split('/')
        else:
            None

    def splitp(self):
        if self.pros:
            return self.pros.split('/')
        else:
            None

    def splitc(self):
        if self.cons:
            return self.cons.split('/')
        else:
            None