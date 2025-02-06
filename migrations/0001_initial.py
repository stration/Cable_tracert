# cable_tracer/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('dcim', '0200_populate_mac_addresses'),  # Зависимость от dcim (замените на актуальную версию)
    ]

    operations = [
        migrations.CreateModel(
            name='CableTrace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('start_port', models.CharField(max_length=100)),
                ('end_port', models.CharField(max_length=100)),
                ('path', models.JSONField()),
                ('start_device', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='start_traces', to='dcim.device')),
                ('end_device', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='end_traces', to='dcim.device')),
            ],
        ),
    ]
