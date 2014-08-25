# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0024_auto_20140821_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='itype',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='name',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='seriousness',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='time_effect',
        ),
    ]
