from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import NFTSerializer
from .serializers import UserSerializer
from .models import NFT
from .models import Users


class NFTList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer  # tell django what serializer to use


class NFTDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NFT.objects.all().order_by('id')
    serializer_class = NFTSerializer


class UsersList(generics.ListCreateAPIView):
    # tell django how to retrieve all objects from the DB, order by id ascending
    queryset = Users.objects.all().order_by('id')
    serializer_class = UserSerializer  # tell django what serializer to use


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UserSerializer
