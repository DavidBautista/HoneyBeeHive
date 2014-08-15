# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0019_auto_20140815_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beetask',
            name='description',
            field=models.TextField(max_length=1024),
        ),
    ]
