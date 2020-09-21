# Django Core
from django.urls import path

# Owner
from .views import SignAuth, Users, UserProfile


accounts_v1_urls = [
    path("v1/login", SignAuth.as_view(), name="login"),
    path("v1/users/<int:pk>", Users.as_view(), name="user"),
    path("v1/users/profile/<str:uuid>", UserProfile.as_view(), name="user-profile"),
]
