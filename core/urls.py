from rest_framework.routers import SimpleRouter
from .views import ItemsView


router = SimpleRouter()

router.register('items', ItemsView)


urlpatterns = []

urlpatterns += router.urls
