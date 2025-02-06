# cable_tracer/navigation.py
from netbox.plugins import PluginMenuItem

menu_items = (
   PluginMenuItem(
        link='plugins:cable_tracer:cabletrace_list',  # Используйте формат plugins:<plugin_name>:<route_name>
        link_text='Cable Traces',
        permissions=['cable_tracer.view_cabletrace'],  # Разрешения для просмотра страницы
    ),
)
