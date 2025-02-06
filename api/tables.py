import django_tables2 as tables
from .models import CableTrace

class CableTraceTable(tables.Table):
    start_device = tables.Column(linkify=True)
    end_device = tables.Column(linkify=True)

    class Meta:
        model = CableTrace
        fields = ('start_device', 'start_port', 'end_device', 'end_port')
