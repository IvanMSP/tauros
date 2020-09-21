# Django Core
from django.urls import path

# Owner
from .views import SignAuth, UserUpdate


accounts_v1_urls = [
    path("v1/login", SignAuth.as_view(), name="login"),
    path("v1/users/<int:pk>", UserUpdate.as_view(), name="user"),
]
