# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-08 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170423_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='alien',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to='avatar', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferred_lang',
            field=models.CharField(choices=[('c', 'C'), ('cpp', 'C++'), ('python', 'Python 3'), ('java', 'Java 8')], default='cpp', max_length=12, verbose_name='preferred language'),
        ),
    ]
