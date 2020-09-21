# Django Core
from django.db import models


class TimeStampModel(models.Model):
    """
    Model for fields TimeStamp
    """

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
