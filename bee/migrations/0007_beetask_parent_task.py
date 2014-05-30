# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0006_assignedworkertotask_ttask'),
    ]

    operations = [
        migrations.AddField(
            model_name='beetask',
            name='parent_task',
            field=models.ForeignKey(to='bee.BeeTask', to_field='id'),
            preserve_default=True,
        ),
    ]
