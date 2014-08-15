# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0017_auto_20140815_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beetask',
            name='pred_end_date',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='pred_start_date',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='real_end_date',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='real_start_date',
            field=models.TimeField(null=True),
        ),
    ]
