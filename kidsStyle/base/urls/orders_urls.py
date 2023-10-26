from django.urls import path
from base.views.orders_views import OrderItemCreateView, OrderItemListView, OrderItemUpdateQtyView, OrderItemDeleteView


urlpatterns = [
    path('create', view=OrderItemCreateView.as_view(), name='create order item'),
    path('', view=OrderItemListView.as_view(), name='getAllOrderItemsForUser'),
    path('<str:pk>', view=OrderItemUpdateQtyView.as_view(), name='updateQty'),
    path('delete/<str:pk>', view=OrderItemDeleteView.as_view(), name='updateQty'),

]
