from netbox.plugins import PluginConfig
from .version import __version__

class CableTracertConfig(PluginConfig):
    name = 'cable_tracert'
    verbose_name = 'Cable Tracer'
    description = 'A plugin to trace cables to their endpoints in NetBox.'
    version = '0.1'
    author = 'Igor Mentoyan'
    author_email = 'stration75@gmail.com'
    base_url = 'cable-tracert'
    min_version = '4.1.0'
    max_version = '4.2.99'

config = CableTracertConfig
