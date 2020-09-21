# Django Core
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Thirdy Party
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
# Owner
from reusable.response import EnvelopeResponse
from .serializers import UserBaseSerializer, UserUpdateSerializer
from ...models import Profile


class SignAuth(APIView):
    """
        View for register/login User
    """
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        user, created = User.objects.get_or_create(username=username)
        if created is True:
            response_status = status.HTTP_201_CREATED
            user.email = data.get('email')
            Profile.objects.create(owner=user)
            user.save()
        else:
            response_status = status.HTTP_200_OK
        serializer = UserBaseSerializer(user)
        return EnvelopeResponse(serializer.data, status=response_status)


class UserUpdate(RetrieveUpdateAPIView):
    """
        View for Update data User
        endpoint: v1/users/<int:pk>
    """
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
