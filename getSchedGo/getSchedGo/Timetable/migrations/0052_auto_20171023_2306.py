# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 17:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timetable', '0051_merge_20171023_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='DeadLineDate',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 26), null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Duration',
            field=models.CharField(choices=[('1', 'Half Hour'), ('2', 'One Hour'), ('3', 'One and Half Hour'), ('4', 'Two Hour'), ('5', 'Two and Half Hour'), ('6', 'Three Hour'), ('7', 'Three and HalfHour'), ('8', 'Four Hour')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='instructorassignment',
            name='DeadLineDate',
            field=models.DateField(blank=True, default=datetime.date(2017, 10, 26), null=True),
        ),
        migrations.AlterField(
            model_name='instructorassignment',
            name='ExpectedDuration',
            field=models.CharField(choices=[('1', 'Half Hour'), ('2', 'One Hour'), ('3', 'One and Half Hour'), ('4', 'Two Hour'), ('5', 'Two and Half Hour'), ('6', 'Three Hour'), ('7', 'Three and HalfHour'), ('8', 'Four Hour')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='instructorexam',
            name='PreparationDuration',
            field=models.CharField(blank=True, choices=[('1', 'Half Hour'), ('2', 'One Hour'), ('3', 'One and Half Hour'), ('4', 'Two Hour'), ('5', 'Two and Half Hour'), ('6', 'Three Hour'), ('7', 'Three and HalfHour'), ('8', 'Four Hour')], default='1', max_length=5, null=True),
        ),
    ]