from rest_framework import serializers

from parties.models import Party

from taggit.serializers import TagListSerializerField, TaggitSerializer


class PartySerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Party
        fields = '__all__'
