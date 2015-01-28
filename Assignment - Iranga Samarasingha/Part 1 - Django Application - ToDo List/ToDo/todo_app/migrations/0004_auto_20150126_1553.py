# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20150126_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 22, 53, 9, 922000, tzinfo=utc), verbose_name=b'Date Assigned'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 22, 53, 15, 218000, tzinfo=utc), verbose_name=b'Due Date'),
            preserve_default=False,
        ),
    ]
