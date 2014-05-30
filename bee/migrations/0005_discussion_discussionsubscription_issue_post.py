# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bee', '0004_assignedworkertotask_beetask_sprint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=140)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(to='bee.Project', to_field='id')),
                ('sprint', models.ForeignKey(to='bee.Sprint', to_field='id', null=True)),
                ('task', models.ForeignKey(to='bee.BeeTask', to_field='id', null=True)),
                ('started_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seriousness', models.SmallIntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('name', models.CharField(max_length=140)),
                ('itype', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=1024)),
                ('time_effect', models.DateTimeField(null=True)),
                ('ttask', models.ForeignKey(to='bee.BeeTask', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiscussionSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('discussion', models.ForeignKey(to='bee.Discussion', to_field='id')),
                ('new_messages', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=140)),
                ('content', models.CharField(max_length=1024)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('discussion', models.ForeignKey(to='bee.Discussion', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
