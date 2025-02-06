# cable_tracer/plugin_config.py
from netbox.plugins import PluginConfig

class CableTracertConfig(PluginConfig):
    name = 'cable_tracer'
    verbose_name = 'Cable Tracer'
    description = 'A plugin to trace cables to their endpoints in NetBox.'
    version = '0.1'
    base_url = 'cable-tracert'  # Префикс для всех маршрутов плагина

config = CableTracertConfig
