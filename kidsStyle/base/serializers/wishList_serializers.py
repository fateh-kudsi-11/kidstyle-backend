from rest_framework import serializers
from base.models.wish_list import WishListItem
from base.serializers.product_serializers import ProductSerializer


class WishListItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishListItem
        fields = '__all__'
