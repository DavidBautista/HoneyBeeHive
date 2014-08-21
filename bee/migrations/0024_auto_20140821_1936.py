# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0023_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskWorkingTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('btask', models.ForeignKey(to='bee.BeeTask', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='assignedworkertotask',
            name='ttask',
        ),
        migrations.RemoveField(
            model_name='assignedworkertotask',
            name='uworker',
        ),
        migrations.DeleteModel(
            name='AssignedWorkerToTask',
        ),
        migrations.AddField(
            model_name='beetask',
            name='assigned_user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beetask',
            name='status',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Prepared'), (2, 'Working'), (3, 'Paused'), (4, 'Finished')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beetask',
            name='time_worked',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='beetask',
            name='parent_task',
        ),
    ]
