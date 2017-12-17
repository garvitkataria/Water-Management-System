# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-06 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('s_type', models.CharField(choices=[('WL', 'Water Level'), ('Temp', 'Temperature'), ('SM', 'Soil Moisture'), ('HDT', 'Humidity')], default='Temp', max_length=20)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
            ],
        ),
    ]
