# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-25 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0006_beta_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beta',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
