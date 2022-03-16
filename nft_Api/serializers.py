from rest_framework import serializers
from .models import NFT


# serializers.ModelSerializer just tells django to convert sql to JSON
class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT  # tell django which model to use
        # tell django which fields to include
        fields = ('id', 'image', 'name', 'price', 'description', 'properties',)
