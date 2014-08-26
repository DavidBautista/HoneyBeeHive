# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bee', '0025_auto_20140825_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='NikoMood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mood', models.SmallIntegerField(default=2, choices=[(1, 'Green'), (2, 'Yellow'), (3, 'Red')])),
                ('date', models.DateField(auto_now_add=True)),
                ('project', models.ForeignKey(to='bee.Project')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
