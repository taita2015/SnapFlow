# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 08:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0034_thread_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userthreadstatus',
            old_name='collected',
            new_name='answering_count',
        ),
        migrations.RenameField(
            model_name='userthreadstatus',
            old_name='disliked',
            new_name='being_collected_count',
        ),
        migrations.RenameField(
            model_name='userthreadstatus',
            old_name='liked',
            new_name='being_disliked_count',
        ),
        migrations.RenameField(
            model_name='userthreadstatus',
            old_name='reply_open',
            new_name='being_liked_count',
        ),
        migrations.RenameField(
            model_name='userthreadstatus',
            old_name='thread_open',
            new_name='question_count',
        ),
    ]
