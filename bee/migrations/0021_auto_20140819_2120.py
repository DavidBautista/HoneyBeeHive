# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0020_auto_20140815_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='response_to',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subject',
        ),
    ]
