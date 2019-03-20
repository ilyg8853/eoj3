# Generated by Django 2.1.7 on 2019-03-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polygon', '0017_auto_20190305_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='status',
            field=models.IntegerField(choices=[(-1, '已终止'), (0, '正在编辑'), (1, '已完成')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='template',
            name='language',
            field=models.CharField(choices=[('c', 'C'), ('cpp', 'C++11'), ('cc14', 'C++14'), ('cc17', 'C++17'), ('py2', 'Python 2'), ('python', 'Python 3'), ('pypy', 'PyPy'), ('pypy3', 'PyPy 3'), ('java', 'Java 8'), ('pas', 'Pascal'), ('scala', 'Scala'), ('text', 'Text')], default='cpp', max_length=12, verbose_name='语言'),
        ),
    ]