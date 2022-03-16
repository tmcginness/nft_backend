from .models import Users
from django.contrib import admin
from .models import NFT

# Register your models here.

admin.site.register(NFT)

admin.site.register(Users)
