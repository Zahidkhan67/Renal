# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 16:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180925_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logdetails',
            name='email',
        ),
    ]
