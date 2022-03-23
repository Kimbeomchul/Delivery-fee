from rest_framework import serializers

from comments.models import Comment
from common.serializers import DisableUpdateUserMixin

class CommentSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.name