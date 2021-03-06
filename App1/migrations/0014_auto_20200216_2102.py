# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-02-16 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0013_user_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_post',
            name='video',
        ),
        migrations.AlterField(
            model_name='friend',
            name='friends',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(default='propfile_pics\\download_1.jpg', upload_to='propfile_pics'),
        ),
    ]
