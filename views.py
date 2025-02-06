# cable_tracer/views.py
from netbox.views import generic
from cable_tracer.models import CableTrace  # Абсолютный импорт
from cable_tracer.tables import CableTraceTable
from cable_tracer.forms import CableTraceForm

class CableTraceListView(generic.ObjectListView):
    queryset = CableTrace.objects.all()
    table = CableTraceTable

class CableTraceView(generic.ObjectView):
    queryset = CableTrace.objects.all()

class CableTraceEditView(generic.ObjectEditView):
    queryset = CableTrace.objects.all()
    form = CableTraceForm

class CableTraceDeleteView(generic.ObjectDeleteView):
    queryset = CableTrace.objects.all()
