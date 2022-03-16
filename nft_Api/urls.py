from django.urls import path
from . import views

urlpatterns = [
    # api/nfts will be routed to the NFTList view for handling
    path('api/nfts', views.NFTList.as_view(), name='nft_list'),
    # api/NFTs will be routed to the NFTDetail view for handling
    path('api/nfts/<int:pk>', views.NFTDetail.as_view(), name='nft_detail'),
    # api/users will be routed to the UserList view for handling
    path('api/user', views.UserList.as_view(), name='user_list'),
    # api/Users will be routed to the UserDetail view for handling
    path('api/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

]
