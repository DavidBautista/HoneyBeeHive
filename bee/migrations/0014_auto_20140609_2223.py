# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0013_userstory_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='project',
            field=models.ForeignKey(to='bee.Project', to_field='id'),
        ),
    ]
