from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from parties.models import Party, Participant
from common.serializers import DisableUpdateUserMixin


class PartySerializer(TaggitSerializer, DisableUpdateUserMixin, serializers.ModelSerializer):
    tags = TagListSerializerField()
    nickname = serializers.SerializerMethodField()

    class Meta:
        model = Party
        fields = '__all__'

    def get_nickname(self, obj):
        return obj.user.nickname
        
class ParticipantsSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        return response
