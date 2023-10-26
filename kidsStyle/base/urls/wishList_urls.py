from django.urls import path
from base.views.wishList_views import CreateWishListItem, DeleteWishListItem, GetUserWishList, GetUserWishListProduct


urlpatterns = [
    path('create', view=CreateWishListItem.as_view(), name='create wish List'),
    path('delete', view=DeleteWishListItem.as_view(), name='delete wish List'),
    path('', view=GetUserWishList.as_view(),
         name='get all wish list product IDs'),
    path('products', view=GetUserWishListProduct.as_view(),
         name='get all wish list product'),
]
