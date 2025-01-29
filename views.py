from netbox.views import generic
from .models import CableTrace
from .tables import CableTraceTable
from .forms import CableTraceForm

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
