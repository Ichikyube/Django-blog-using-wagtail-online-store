# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-03 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectviewed',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Object viewed', 'verbose_name_plural': 'Objects viewed'},
        ),
    ]
