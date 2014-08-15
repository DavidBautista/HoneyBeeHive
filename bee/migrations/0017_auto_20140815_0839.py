# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0016_beetask_time_prevision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beetask',
            name='parent_task',
            field=models.ForeignKey(to='bee.BeeTask', null=True),
        ),
    ]
