from rest_framework import serializers

from comments.models import Comment
from common.serializers import DisableUpdateUserMixin

class CommentSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
