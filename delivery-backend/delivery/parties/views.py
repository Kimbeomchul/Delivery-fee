from rest_framework import viewsets
from rest_framework.response import Response

from parties.models import Party, Participant
from parties.serializers import PartySerializer, ParticipantsSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantsSerializer
