# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20150126_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignedby',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='assignedto',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
