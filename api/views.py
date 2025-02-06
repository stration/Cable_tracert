# cable_tracer/api/views.py
from netbox.api.viewsets import NetBoxModelViewSet
from cable_tracer.models import CableTrace  # Используйте абсолютный импорт
from .serializers import CableTraceSerializer

class CableTraceViewSet(NetBoxModelViewSet):
    queryset = CableTrace.objects.all()
    serializer_class = CableTraceSerializer
