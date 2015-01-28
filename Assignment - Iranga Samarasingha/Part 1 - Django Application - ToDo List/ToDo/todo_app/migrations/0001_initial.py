# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('completed', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
