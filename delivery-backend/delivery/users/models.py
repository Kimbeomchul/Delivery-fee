from django.db import models
from django.contrib.auth.models import AbstractUser

from common.models import Timestampable

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser, Timestampable):
    name = models.CharField(max_length=200, help_text='사용자 이름')
    phone_number = PhoneNumberField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
