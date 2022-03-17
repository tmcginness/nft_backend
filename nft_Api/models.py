from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class NFT(models.Model):
    image = models.TextField(default="none")
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.TextField()
    offer = models.BooleanField(default=False)
    offer_price = models.IntegerField(default=0)
    owner = models.CharField(max_length=64, default="None")
    blockchain = models.CharField(max_length=16, default="Ethereum")
    collection = models.CharField(max_length=32, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)


class User(models.Model):
    image = models.TextField(default="none")
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    password = models.CharField(max_length=50)
    collected = models.TextField(blank=True, null=True)
    created = models.TextField(blank=True, null=True)
    favorited = models.TextField(blank=True, null=True)
    offers = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
