# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20170410_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subclass',
            options={'ordering': ['parent_class'], 'verbose_name': '子帖子类型', 'verbose_name_plural': '子帖子类型'},
        ),
    ]
