from django.db import models

from datetime import datetime
from realtors.models import Realtor

# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    sqrt = models.ImageField()
    bathrooms = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%M/%D')
    photo_1 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%M/%D', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)