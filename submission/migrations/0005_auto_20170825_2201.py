# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20170729_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='code_length',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='judge_start_time',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='status_memory',
        ),
        migrations.AddField(
            model_name='submission',
            name='status_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='status_private',
            field=models.IntegerField(choices=[(-4, 'Submitted'), (-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong Answer'), (0, 'Accepted'), (1, 'Time Limit Exceeded'), (2, 'Idleness Limit Exceeded'), (3, 'Memory Limit Exceeded'), (4, 'Runtime Error'), (5, 'System Error'), (6, 'Compile Error'), (7, 'Idleness Limit Exceeded'), (8, 'Time Limit Exceeded'), (11, 'Judge Error'), (12, 'Pretest Passed')], default=-4),
        ),
        migrations.AlterField(
            model_name='submission',
            name='lang',
            field=models.CharField(choices=[('c', 'C'), ('cpp', 'C++11'), ('python', 'Python 3'), ('java', 'Java 8'), ('cc14', 'C++14'), ('cs', 'C#'), ('py2', 'Python 2'), ('php', 'PHP 7'), ('perl', 'Perl'), ('hs', 'Haskell'), ('js', 'Javascript'), ('ocaml', 'OCaml'), ('pypy', 'PyPy'), ('pas', 'Pascal'), ('rs', 'Rust')], default='cpp', max_length=12, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.IntegerField(choices=[(-4, 'Submitted'), (-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong Answer'), (0, 'Accepted'), (1, 'Time Limit Exceeded'), (2, 'Idleness Limit Exceeded'), (3, 'Memory Limit Exceeded'), (4, 'Runtime Error'), (5, 'System Error'), (6, 'Compile Error'), (7, 'Idleness Limit Exceeded'), (8, 'Time Limit Exceeded'), (11, 'Judge Error'), (12, 'Pretest Passed')], default=-4),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status_time',
            field=models.FloatField(default=0),
        ),
    ]
