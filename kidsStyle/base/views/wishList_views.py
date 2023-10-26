from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base.models.wish_list import WishListItem
from base.serializers.wishList_serializers import WishListItemSerializer
from rest_framework.permissions import IsAuthenticated
from base.models.products_model import Product


class CreateWishListItem(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Check if the required fields are present in the request data
        required_fields = ['product']
        for field in required_fields:
            if field not in request.data:
                message = {'detail': f'Missing {field} in request data'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = request.user
            product_id = request.data['product']

            # Fetch the Product instance using the provided product_id
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'detail': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Check if the user already has the product in their wish list
            if WishListItem.objects.filter(user=user, product=product).exists():
                return Response({'detail': 'Product already in the wish list.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new wish list item
            wish_list_item = WishListItem.objects.create(
                user=user, product=product)

            # Serialize the created wish list item
            serializer = WishListItemSerializer(wish_list_item)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteWishListItem(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        # Check if the required field "product" is present in the request data
        if 'product' not in request.data:
            message = {'detail': 'Missing product in request data'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = request.user
            product_id = request.data['product']

            # Check if the user has the product in their wish list
            try:
                wish_list_item = WishListItem.objects.get(
                    user=user, product=product_id)
            except WishListItem.DoesNotExist:
                return Response({'detail': 'Product not found in the wish list.'}, status=status.HTTP_404_NOT_FOUND)

            # Delete the wish list item
            wish_list_item.delete()

            return Response({'detail': 'Product removed from the wish list.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetUserWishList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        try:
            user = request.user
            # Retrieve all product IDs from the user's wish list
            product_ids = WishListItem.objects.filter(
                user=user).values_list('product', flat=True)
            return Response(product_ids, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetUserWishListProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            # Retrieve all wish list items for the user
            wish_list_items = WishListItem.objects.filter(user=user)
            serializer = WishListItemSerializer(wish_list_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
