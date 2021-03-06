# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20171007_0124'),
        ('myauth', '0008_auto_20171001_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('calendario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.Calendar')),
                ('jefe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
