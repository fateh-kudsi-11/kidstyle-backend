from rest_framework.views import APIView
from rest_framework.response import Response
from base.models.products_model import Product
from base.serializers.product_serializers import ProductSerializer
from rest_framework import status

# Create your views here.


class GetRoutes(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        return Response("Hello")


class GetProducts(APIView):
    def get(self, request, format=None):
        sort_by = request.query_params.get('sort', None)
        gender = request.query_params.get('gender', None)
        category = request.query_params.get('category', None)

        products = Product.objects.all()

        if gender and category:
            products = products.filter(
                gender=gender, category__category=category)
        elif gender:
            products = products.filter(gender=gender)
        elif category:
            products = products.filter(category__category=category)

        if sort_by:
            if sort_by == 'popular':
                products = products.order_by('-watchCount')
            elif sort_by == 'highToLow':
                products = products.order_by('-price')
            elif sort_by == 'lowToHigh':
                products = products.order_by('price')

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetProduct(APIView):
    def get(self, request, pk, format=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.watchCount += 1
        product.save()

        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
