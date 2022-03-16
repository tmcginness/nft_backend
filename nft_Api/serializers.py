from rest_framework import serializers
from .models import NFT
from .models import User


# serializers.ModelSerializer just tells django to convert sql to JSON
class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT  # tell django which model to use
        # tell django which fields to include
        fields = ('id', 'image', 'name', 'price', 'description', 'properties',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # tell django which model to use
        # tell django which fields to include
        fields = ('id', 'image', 'fname', 'lname', 'password',
                  'collection', 'offers', 'properties',)
