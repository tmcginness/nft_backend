from django.db import models

# Create your models here.


class NFT(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.TextField()
    properties = models.TextField()
