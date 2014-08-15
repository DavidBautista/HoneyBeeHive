# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0014_auto_20140609_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedworkertoproject',
            name='permissions',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Read'), (2, 'Write'), (3, 'Admin')]),
            preserve_default=True,
        ),
    ]
