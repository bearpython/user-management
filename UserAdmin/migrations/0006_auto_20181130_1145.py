# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-30 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAdmin', '0005_auto_20181130_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='utime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
