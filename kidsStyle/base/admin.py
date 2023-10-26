from django.contrib import admin
from base.models.products_model import Product, ProductSize, ProductColor, ProductImage, ProductDetails, ProductCategory, ProductType, ProductBrand
from base.models.orders_model import OrderItem
from base.models.wish_list import WishListItem


class MyModelAdmin(admin.ModelAdmin):

    ordering = ('-created_at',)
    search_fields = ['id']


class MyModelProductAdmin(admin.ModelAdmin):
    ordering = ('-createAt',)
    search_fields = ['id', 'productName']


class MyModelOrderAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    search_fields = ['id']


class MyModelWishListAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    search_fields = ['id']


admin.site.register(Product, MyModelProductAdmin)
admin.site.register(ProductBrand, MyModelAdmin)
admin.site.register(ProductSize, MyModelAdmin)
admin.site.register(ProductColor, MyModelAdmin)
admin.site.register(ProductImage, MyModelAdmin)
admin.site.register(ProductDetails, MyModelAdmin)
admin.site.register(ProductCategory, MyModelAdmin)
admin.site.register(ProductType, MyModelAdmin)
admin.site.register(OrderItem, MyModelOrderAdmin)
admin.site.register(WishListItem, MyModelWishListAdmin)
