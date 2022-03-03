from django.contrib.gis.db import models

from common.models import Timestampable
from users.models import User
from parties.models import Party


class Comment(Timestampable):
    content = models.TextField(help_text='댓글 내용')
    party = models.ForeignKey(Party, on_delete=models.CASCADE, help_text='댓글이 달린 파티')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='댓글 단 유저')
