from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from base.models.products_model import Product
from base.models.orders_model import OrderItem
from base.serializers.orders_serializers import OrderItemSerializer


class OrderItemCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # Check if the required fields are present in the request data
        required_fields = ['product', 'qty', 'selected_color', 'selected_size']
        for field in required_fields:
            if field not in request.data:
                message = {'detail': f'Missing {field} in request data'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_id = request.data['product']
            qty = request.data['qty']
            selected_color = request.data['selected_color']
            selected_size = request.data['selected_size']

            # Check if the user already has an OrderItem for the same product
            existing_order_item = OrderItem.objects.filter(
                user=request.user,
                product=product_id
            ).first()

            if existing_order_item:
                # If an existing OrderItem exists, delete it
                existing_order_item.delete()

            # Create a new OrderItem
            product = Product.objects.get(id=product_id)
            order_item = OrderItem.objects.create(
                user=request.user,
                product=product,
                qty=qty,
                selected_color=selected_color,
                selected_size=selected_size
            )

            serializer = OrderItemSerializer(order_item, many=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        try:
            order_items = OrderItem.objects.filter(user=request.user)

            serializer = OrderItemSerializer(order_items, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderItemUpdateQtyView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        try:
            # Retrieve the specific OrderItem for the authenticated user
            order_item = OrderItem.objects.get(user=request.user, pk=pk)

            # Check if 'qty' is provided in the request data
            new_qty = request.data.get('qty')

            if new_qty is not None:
                # Update the quantity
                order_item.qty = new_qty
                order_item.save()

                # Serialize the updated order item
                serializer = OrderItemSerializer(order_item)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Missing "qty" in request data'}, status=status.HTTP_400_BAD_REQUEST)
        except OrderItem.DoesNotExist:
            return Response({'detail': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            # Retrieve the specific OrderItem for the authenticated user
            order_item = OrderItem.objects.get(user=request.user, pk=pk)

            # Delete the order item
            order_item.delete()

            return Response({'detail': 'OrderItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({'detail': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
