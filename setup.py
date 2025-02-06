from setuptools import setup, find_packages

setup(
    name='cable_tracer',
    version='0.1.0',  # Установите версию по умолчанию
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Список зависимостей вашего плагина, если они есть
        # 'django>=3.2,<4.0',
    ],
    entry_points={
        'netbox_plugins': [
            'cable_tracer = cable_tracer.plugin_config:CableTracertConfig',  # Замените на вашу точку входа
        ],
    },
)
