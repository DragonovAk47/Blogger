# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-20 14:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0020_auto_20200218_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='App1.User_Post'),
        ),
    ]
