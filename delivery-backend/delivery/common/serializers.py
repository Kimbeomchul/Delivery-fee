from rest_framework import serializers


class DisableUpdateUserMixin(serializers.BaseSerializer):
    def update(self, instance, validated_data):
        if instance.user != validated_data.get('user', instance.user):
            raise serializers.ValidationError("You cannot change users.")
        return super().update(instance, validated_data)
