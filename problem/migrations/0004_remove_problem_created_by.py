# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-18 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_auto_20170417_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='created_by',
        ),
    ]
