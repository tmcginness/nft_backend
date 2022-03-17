from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class NFT(models.Model):
    image = models.TextField(default="none")
    name = models.CharField(max_length=32)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    offer = models.BooleanField(default=False)
    offer_price = models.IntegerField(default=0)
    owner = models.CharField(max_length=64, blank=True, null=True)
    blockchain = models.CharField(max_length=16, default="Ethereum")
    collection = models.CharField(max_length=32, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)


class User(models.Model):
    image = models.TextField(default="none")
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    password = models.CharField(max_length=50)
    collection = models.CharField(
        max_length=200, blank=True, null=True)
    created = models.CharField(
        max_length=200, blank=True, null=True)
    favorited = models.CharField(
        max_length=200, blank=True, null=True)
    offers = models.CharField(
        max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
