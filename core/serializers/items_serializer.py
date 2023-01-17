from rest_framework import serializers
from core.models import Item


class ItemSerializer(serializers.ModelSerializer):

    # filename

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'piture']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        piture = instance.piture.name
        representation['piture'] = piture
        return representation
