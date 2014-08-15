# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0018_auto_20140815_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beetask',
            name='pred_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='pred_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='real_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='beetask',
            name='real_start_date',
            field=models.DateField(null=True),
        ),
    ]
