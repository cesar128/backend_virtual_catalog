from rest_framework import serializers
from core.models import Item


class ItemSerializer(serializers.ModelSerializer):

    # filename

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'picture', 'price', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        picture = instance.picture.name
        representation['picture'] = picture
        return representation
