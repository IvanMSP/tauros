# Django Core
from django.contrib import admin

# Owner
from .models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass
