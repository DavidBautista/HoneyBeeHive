# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0008_discussionsubscription_last_read_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='response_to',
            field=models.ForeignKey(to='bee.Post', to_field='id', null=True),
            preserve_default=True,
        ),
    ]
