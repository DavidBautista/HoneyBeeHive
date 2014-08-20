# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0021_auto_20140819_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussionsubscription',
            name='discussion',
        ),
        migrations.RemoveField(
            model_name='discussionsubscription',
            name='last_read_post',
        ),
        migrations.RemoveField(
            model_name='discussionsubscription',
            name='user',
        ),
        migrations.DeleteModel(
            name='DiscussionSubscription',
        ),
    ]
