from rest_framework import viewsets
from rest_framework.response import Response

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.filter(party=self.kwargs['party_pk'])
