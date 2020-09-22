# Django Core
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Thirdy Party
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
# Owner
from reusable.response import EnvelopeResponse, EnvelopeErrorResponse
from .serializers import UserBaseSerializer, UserUpdateSerializer, UserProfileSerializer
from ...models import Profile
from reusable.constants import NULL_VALUE


class SignAuth(APIView):
    """
    Methods: POST
    View for register/login User
    """

    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        if email in NULL_VALUE or username in NULL_VALUE or password in NULL_VALUE:
            return EnvelopeErrorResponse(
                "Fields are missing", status=status.HTTP_400_BAD_REQUEST
            )
        user, created = User.objects.get_or_create(username=username)
        if created is True:
            response_status = status.HTTP_201_CREATED
            user.email = email
            user.password = make_password(password)
            Profile.objects.create(owner=user)
        else:
            response_status = status.HTTP_200_OK
        serializer = UserBaseSerializer(user)
        user.save()
        return EnvelopeResponse(serializer.data, status=response_status)


class Users(RetrieveUpdateAPIView):
    """
    Methods: GET, PUT, PATCH
    View for Update data User
    endpoint: v1/users/<int:pk>
    """

    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()


class UserProfile(RetrieveUpdateAPIView):
    """
    Methods: GET, PUT, PATCH
    View for update user profile
    endpoint: v1/users/<int:pk>/profile
    """

    lookup_field = "uuid"
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, uuid=self.kwargs.get('uuid'), owner=self.request.user)
        return obj
