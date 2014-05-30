# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bee', '0003_assignedworkertoproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('project', models.ForeignKey(to='bee.Project', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignedWorkerToTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uworker', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('role', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BeeTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('ttype', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=1024)),
                ('pred_start_date', models.DateTimeField(null=True)),
                ('pred_end_date', models.DateTimeField(null=True)),
                ('real_start_date', models.DateTimeField(null=True)),
                ('real_end_date', models.DateTimeField(null=True)),
                ('sprint', models.ForeignKey(to='bee.Sprint', to_field='id')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
