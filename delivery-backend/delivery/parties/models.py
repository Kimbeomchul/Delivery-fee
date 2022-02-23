from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from taggit.managers import TaggableManager

from users.models import User
from common.models import Timestampable


class Party(Timestampable):
    title = models.CharField(max_length=30, help_text='파티 제목')
    tags = TaggableManager()
    order_time = models.DateTimeField()
    content = models.TextField(help_text='파티 내용')
    location = models.PointField(default=Point(0.0, 0.0))
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='파티 주최자')
    participants = ArrayField(models.IntegerField(), default=list, help_text='파티 참여자 명단')
