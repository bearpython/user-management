# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-27 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('utime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(help_text='input password', max_length=64)),
                ('email', models.EmailField(max_length=19, null=True)),
                ('testurl', models.URLField(max_length=19, null=True)),
                ('testip', models.GenericIPAddressField(null=True)),
                ('user_type_id', models.IntegerField(choices=[(1, '超级用户'), (2, '普通用户'), (3, '开发用户')], default=1)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAdmin.UserGroup')),
            ],
        ),
    ]
