# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 17:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_logintime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoginTime',
            new_name='LogDetails',
        ),
    ]
