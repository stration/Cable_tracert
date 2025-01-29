from rest_framework import serializers
from .models import CableTrace

class CableTraceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CableTrace
        fields = '__all__'
