# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20150126_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignedby',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Assigned By', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='assignedto',
            field=models.CharField(max_length=30, null=True, verbose_name=b'Assigned To', blank=True),
            preserve_default=True,
        ),
    ]
