# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-09 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visible'),
        ),
    ]
