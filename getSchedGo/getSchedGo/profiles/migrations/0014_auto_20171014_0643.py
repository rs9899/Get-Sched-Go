# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 01:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_profile_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lastSuggestion',
            field=models.DateField(default=datetime.date(2017, 10, 9), null=True),
        ),
    ]
