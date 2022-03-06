from rest_framework import serializers

from parties.models import Party, Participant

from taggit.serializers import TagListSerializerField, TaggitSerializer


class PartySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Party
        fields = '__all__'
        
        
class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
