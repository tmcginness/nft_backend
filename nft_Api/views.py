from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import NFTSerializer
from .serializers import UserSerializer
from .models import NFT
from .models import User


class NFTList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer  # tell django what serializer to use


class NFTDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer


class UserList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer  # tell django what serializer to use


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
