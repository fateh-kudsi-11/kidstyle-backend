from base.models.products_model import Product, ProductSize, ProductColor, ProductImage, ProductDetails
from rest_framework import serializers
from collections import defaultdict


class ProductSizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['size']
        ordering = ['-created_at']


class ProductColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['colorCode', 'color']
        ordering = ['-created_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'color']
        ordering = ['-created_at']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
        ordering = ['-created_at']


class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()
    colors = ProductColorSerializers(many=True)
    images = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()
    brand = serializers.CharField(source='brand.brand')
    category = serializers.CharField(source='category.category')
    productType = serializers.CharField(source='productType.type')

    def get_images(self, obj):
        # Retrieve and serialize related images
        images_queryset = obj.images.all()  # Get related images for the product
        images_serializer = ProductImageSerializer(images_queryset, many=True)
        # Group images by color
        images_by_color = defaultdict(list)
        for image_data in images_serializer.data:
            color = image_data['color']
            images_by_color[color].append(image_data)

        return dict(images_by_color)

    def get_details(self, obj):
        details_queryset = obj.details.all()
        detail_strings = list(
            details_queryset.values_list('detail', flat=True))
        return detail_strings

    def get_sizes(self, obj):
        # Retrieve and serialize sizes as a list of size strings
        sizes_queryset = obj.sizes.all().order_by('created_at')
        size_strings = list(sizes_queryset.values_list('size', flat=True))
        return size_strings

    class Meta:
        model = Product
        fields = '__all__'
        ordering = ['-created_at']
