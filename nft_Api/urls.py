from django.urls import path
from . import views

urlpatterns = [
    # api/nfts will be routed to the NFTList view for handling
    path('api/nfts', views.NFTList.as_view(), name='nft_list'),
    # api/NFTs will be routed to the NFTDetail view for handling
    path('api/nfts/<int:pk>', views.NFTDetail.as_view(), name='nft_detail'),
]
