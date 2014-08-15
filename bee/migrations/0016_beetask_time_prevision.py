# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0015_assignedworkertoproject_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='beetask',
            name='time_prevision',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
    ]
