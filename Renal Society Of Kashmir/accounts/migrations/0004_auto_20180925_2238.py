# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinformationdetails_creationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationdetails',
            name='creationTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
