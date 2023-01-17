from rest_framework.viewsets import ReadOnlyModelViewSet

from core.serializers import ItemSerializer
from ..models import Item


class ItemsView(ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(show=True)
