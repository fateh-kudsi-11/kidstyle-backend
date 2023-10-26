from rest_framework import serializers
from base.models.orders_model import OrderItem
from base.serializers.product_serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product_info = ProductSerializer(source='product', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_info', 'user', 'qty',
                  'selected_color', 'selected_size', 'created_at', 'id']
