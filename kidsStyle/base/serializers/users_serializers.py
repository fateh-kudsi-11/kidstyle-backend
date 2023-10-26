from rest_framework import serializers


from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import update_session_auth_hash


class UserSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    firstName = serializers.SerializerMethodField(read_only=True)
    lastName = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'firstName', 'lastName']

    def get_firstName(self, obj):
        firstName = obj.first_name
        return firstName

    def get_lastName(self, obj):
        lastName = obj.last_name
        return lastName

    def get_id(self, obj):
        id = obj.id
        return id


class UserSerializersWithToken(UserSerializers):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'firstName', 'token', 'lastName']

    def get_token(self, obj):
        token = AccessToken.for_user(obj)
        return str(token)


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name', required=False)
    lastName = serializers.CharField(source='last_name', required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']

    def update(self, instance, validated_data):
        # Map the 'firstName' and 'lastName' fields to 'first_name' and 'last_name'
        if 'firstName' in validated_data:
            instance.first_name = validated_data['firstName']
            del validated_data['firstName']

        if 'lastName' in validated_data:
            instance.last_name = validated_data['lastName']
            del validated_data['lastName']

        # Map the 'email' field to 'username'
        if 'email' in validated_data:
            instance.email = validated_data['email']
            instance.username = validated_data['email']

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class UserPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("The old password is incorrect.")
        return value

    def validate_new_password(self, value):
        # You can add validation for the new password here if needed.
        return value

    def save(self, validated_data):
        user = self.context['request'].user
        new_password = validated_data['new_password']
        user.set_password(new_password)
        user.save()
        # Update the session authentication hash
        update_session_auth_hash(self.context['request'], user)
