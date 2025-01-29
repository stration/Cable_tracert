from netbox.api.routers import NetBoxRouter
from .views import CableTraceViewSet

router = NetBoxRouter()
router.register('cable-traces', CableTraceViewSet)

urlpatterns = router.urls
