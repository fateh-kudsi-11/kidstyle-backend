from django.urls import path
from base.views.products_views import GetProducts, GetProduct


urlpatterns = [
    path('', view=GetProducts.as_view(), name='getAllProducts'),
    path('<str:pk>', view=GetProduct.as_view(), name='product'),
]
