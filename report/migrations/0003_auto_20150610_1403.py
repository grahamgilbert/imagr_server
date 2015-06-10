# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computer',
            options={'get_latest_by': 'date_added'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-date_added'], 'get_latest_by': 'date_added'},
        ),
        migrations.AddField(
            model_name='computer',
            name='current_status',
            field=models.CharField(default=b'in_progress', max_length=200),
            preserve_default=False,
        ),
    ]
