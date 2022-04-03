from rest_framework import serializers

from users.models import User
from parties.serializers import ParticipantsSerializer


class UserSerializer(serializers.ModelSerializer):
    participant = ParticipantsSerializer()

    class Meta:
        model = User
        exclude = ['password']