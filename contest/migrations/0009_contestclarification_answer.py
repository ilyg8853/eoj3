# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_auto_20170429_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestclarification',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
