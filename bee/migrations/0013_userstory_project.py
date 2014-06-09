# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0012_auto_20140604_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='project',
            field=models.ForeignKey(to='bee.Project', default=None, to_field='id'),
            preserve_default=True,
        ),
    ]
