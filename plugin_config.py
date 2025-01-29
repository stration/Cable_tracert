from netbox.plugins import PluginConfig

class CableTracertConfig(PluginConfig):
    name = 'cable_tracert'
    verbose_name = 'Cable Tracer'
    description = 'A plugin to trace cables to their endpoints in NetBox.'
    version = '0.1'
    base_url = 'cable-tracert'

config = CableTracertConfig
