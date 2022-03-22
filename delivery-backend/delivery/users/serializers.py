from rest_framework import serializers

from users.models import User
from common.serializers import DisableUpdateUserMixin
from parties.serializers import ParticipantsSerializer


class UserSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    participant = ParticipantsSerializer()

    class Meta:
        model = User
        fields = '__all__'
        