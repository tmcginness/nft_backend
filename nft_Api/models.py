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
<<<<<<< HEAD
    owner = models.CharField(max_length=64, default="None")
=======
    owner = models.CharField(max_length=64, blank=True, null=True)
>>>>>>> 8edee7982d370f5c93ef88e88d04a00192314b87
    blockchain = models.CharField(max_length=16, default="Ethereum")
    collection = models.CharField(max_length=32, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)


class User(models.Model):
    image = models.TextField(default="none")
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    password = models.CharField(max_length=50)
<<<<<<< HEAD
    collected = models.TextField(blank=True, null=True)
    created = models.TextField(blank=True, null=True)
    favorited = models.TextField(blank=True, null=True)
    offers = models.TextField(blank=True, null=True)
=======
    collection = models.CharField(
        max_length=200, blank=True, null=True)
    created = models.CharField(
        max_length=200, blank=True, null=True)
    favorited = models.CharField(
        max_length=200, blank=True, null=True)
    offers = models.CharField(
        max_length=200, blank=True, null=True)
>>>>>>> 8edee7982d370f5c93ef88e88d04a00192314b87
    bio = models.TextField(blank=True, null=True)
