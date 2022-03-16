from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class NFT(models.Model):
    image = models.TextField(default="none")
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.TextField()
    properties = ArrayField(models.CharField(max_length=50), blank=True)
    offer = models.BooleanField(default=False)


class Users(models.Model):
    image = models.TextField(default="none")
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    password = models.CharField(max_length=50)
    collection = ArrayField(models.CharField(max_length=200), blank=True)
    offers = ArrayField(models.CharField(max_length=200), blank=True)
    properties = models.TextField()
