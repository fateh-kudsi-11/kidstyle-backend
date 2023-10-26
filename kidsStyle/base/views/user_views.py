from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from base.serializers.users_serializers import UserSerializersWithToken, UserProfileUpdateSerializer, UserPasswordUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        serailizer = UserSerializersWithToken(self.user).data
        for k, v in serailizer.items():
            data[k] = v
        return data


class RegisterUser(APIView):
    def post(self, request, format=None):
        data = request.data

        # Check if required fields are present in request.data
        required_fields = ['firstName', 'lastName', 'email', 'password']
        for field in required_fields:
            if field not in data:
                message = {'detail': f'Missing {field} in request data'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                first_name=data['firstName'],
                last_name=data['lastName'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )

            serializer = UserSerializersWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        user = request.user

        serializer = UserSerializersWithToken(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):

        serializer = UserProfileUpdateSerializer(
            request.user, data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            # Serialize the updated user data
            user_serializer = UserProfileUpdateSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserPasswordUpdateSerializer(
            context={'request': request}, data=request.data)

        if serializer.is_valid():
            serializer.save(validated_data=request.data)
            return Response("Password updated successfully.", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
