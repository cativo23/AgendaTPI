# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Evntes', '0004_auto_20171002_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customevent',
            name='event_ptr',
        ),
        migrations.DeleteModel(
            name='CustomEvent',
        ),
    ]
