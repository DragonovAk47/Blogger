# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-18 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0019_auto_20200218_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='user_post',
        ),
    ]