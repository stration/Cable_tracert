from django import forms
from .models import CableTrace
from dcim.models import Device

class CableTraceForm(forms.ModelForm):
    class Meta:
        model = CableTrace
        fields = ('start_device', 'start_port', 'end_device', 'end_port')
