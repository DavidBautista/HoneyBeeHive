# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0005_discussion_discussionsubscription_issue_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedworkertotask',
            name='ttask',
            field=models.ForeignKey(to='bee.BeeTask', to_field='id'),
            preserve_default=True,
        ),
    ]
