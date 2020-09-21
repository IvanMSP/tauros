# django Core
from django.contrib.auth.models import User

# Thirdy-Party
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Owner
from ...models import Profile
from ...choices import GENDER_CHOICES


class UserBaseSerializer(serializers.ModelSerializer):
    """
    Serializer User Basic Data
    endpoint: /login
    """

    token = serializers.SerializerMethodField()
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")

    class Meta:
        model = User
        fields = [
            "pk",
            "token",
            "email",
            "firstName",
            "lastName",
        ]

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        if created is False:
            token.delete()
            token = Token.objects.create(user=user)
        return token.key


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to User Profile
    Userd by: UserUpdateSerializer
    """

    uuid = serializers.CharField(read_only=True, required=False)
    created = serializers.CharField(read_only=True)
    modified = serializers.CharField(read_only=True)
    phoneNumber = serializers.CharField(source="phone_number")

    class Meta:
        model = Profile
        fields = [
            "uuid",
            "created",
            "modified",
            "dob",
            "gender",
            "phoneNumber",
            "address",
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer to Update data Of User
    Endpoint: v1/users/<int:pk>
    """

    pk = serializers.CharField(read_only=True, required=False)
    email = serializers.EmailField(read_only=True, required=False)
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = [
            "pk",
            "email",
            "firstName",
            "lastName",
            "profile",
        ]
