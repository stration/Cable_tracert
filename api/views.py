from netbox.api.viewsets import NetBoxModelViewSet
from .models import CableTrace
from .serializers import CableTraceSerializer

class CableTraceViewSet(NetBoxModelViewSet):
    queryset = CableTrace.objects.all()
    serializer_class = CableTraceSerializer
