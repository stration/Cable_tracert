from netbox.search import SearchIndex, register_search
from .models import CableTrace

@register_search
class CableTraceIndex(SearchIndex):
    model = CableTrace
    fields = (
        ('start_device__name', 100),
        ('end_device__name', 100),
    )
