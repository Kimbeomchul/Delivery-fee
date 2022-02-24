from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from common.models import Timestampable

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser, Timestampable):
    name = models.CharField(max_length=200, help_text='사용자 이름')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200, blank=True, help_text='사용자 내위치')
    location = models.PointField(default=Point(0.0, 0.0), help_text='위도 경도')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
