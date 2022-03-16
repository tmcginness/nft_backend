from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import NFTSerializer
from .models import NFT


class NFTList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer  # tell django what serializer to use


class NFTDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer
