# Django Core
import uuid
from django.db import models
from django.contrib.auth.models import User

# Owner
from .choices import GENDER_CHOICES
from reusable.constants import BLANK, REQUIRED
from reusable.models import TimeStampModel


class Profile(TimeStampModel):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dob = models.DateField(**BLANK)
    gender = models.PositiveSmallIntegerField(
        default=1, choices=GENDER_CHOICES, **BLANK
    )
    phone_number = models.CharField(max_length=15, **BLANK)
    address = models.CharField(max_length=150, **BLANK)

    def __str__(self):
        return self.owner.get_full_name()
