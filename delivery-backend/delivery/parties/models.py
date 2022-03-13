from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models

from taggit.managers import TaggableManager

from users.models import User
from common.models import Timestampable


class Party(Timestampable):
    title = models.CharField(max_length=30, help_text='파티 제목')
    tags = TaggableManager()
    order_time = models.DateTimeField()
    content = models.TextField(help_text='파티 내용')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='파티 주최자')

    class Meta:
        ordering = ['-order_time']

class Participant(Timestampable):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, help_text='참가한 파티')
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='참가한 유저')
