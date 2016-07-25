# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-25 01:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0007_auto_20160724_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+0?1\\s)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]\\d{4}$')]),
        ),
    ]
