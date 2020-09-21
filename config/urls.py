# Django Core
from django.contrib import admin
from django.urls import path, include
# Owner
from accounts.api.v1.urls import accounts_v1_urls as accounts_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(accounts_api)),
]
