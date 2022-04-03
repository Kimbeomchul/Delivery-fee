from rest_framework import serializers

from comments.models import Comment
from common.serializers import DisableUpdateUserMixin

class CommentSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    nickname = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_nickname(self, obj):
        return obj.user.nickname