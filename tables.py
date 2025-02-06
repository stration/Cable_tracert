# cable_tracer/tables.py
from netbox.tables import NetBoxTable  # Используйте NetBoxTable для таблиц
from django_tables2 import Column  # Импортируйте Column из django_tables2
from cable_tracer.models import CableTrace  # Абсолютный импорт модели

class CableTraceTable(NetBoxTable):  # Наследование от NetBoxTable
    start_device = Column(linkify=True)  # Колонка с ссылкой
    end_device = Column(linkify=True)  # Колонка с ссылкой

    class Meta:
        model = CableTrace  # Модель для таблицы
        fields = ('start_device', 'start_port', 'end_device', 'end_port')  # Поля для отображения
