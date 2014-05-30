# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('ptype', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1024)),
                ('pred_start_date', models.DateTimeField(null=True)),
                ('pred_end_date', models.DateTimeField(null=True)),
                ('real_start_date', models.DateTimeField(null=True)),
                ('real_end_date', models.DateTimeField(null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
