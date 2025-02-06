# cable_tracer/models.py
from django.db import models
from netbox.models import NetBoxModel  # Используйте NetBoxModel
from dcim.models import Device

class CableTrace(NetBoxModel):  # Наследование от NetBoxModel
    start_device = models.ForeignKey(
        to=Device,
        on_delete=models.CASCADE,
        related_name='start_traces'
    )
    start_port = models.CharField(max_length=100)
    end_device = models.ForeignKey(
        to=Device,
        on_delete=models.CASCADE,
        related_name='end_traces'
    )
    end_port = models.CharField(max_length=100)
    path = models.JSONField()  # Хранение пути в формате JSON

    def __str__(self):
        return f"{self.start_device} -> {self.end_device}"
