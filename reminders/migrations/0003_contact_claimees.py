# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_auto_20160408_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='claimees',
            field=models.ManyToManyField(blank=True, to='reminders.Person'),
        ),
    ]
