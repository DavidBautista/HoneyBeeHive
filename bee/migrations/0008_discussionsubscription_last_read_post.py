# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0007_beetask_parent_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionsubscription',
            name='last_read_post',
            field=models.ForeignKey(to='bee.Post', to_field='id'),
            preserve_default=True,
        ),
    ]
