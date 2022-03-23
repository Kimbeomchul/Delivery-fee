from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from parties.models import Party, Participant
from common.serializers import DisableUpdateUserMixin


class PartySerializer(TaggitSerializer, DisableUpdateUserMixin, serializers.ModelSerializer):
    tags = TagListSerializerField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Party
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.name
        
class ParticipantsSerializer(DisableUpdateUserMixin, serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        return response
