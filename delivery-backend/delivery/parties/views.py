from rest_framework import viewsets
from rest_framework.response import Response

from parties.models import Party
from parties.serializers import PartySerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
