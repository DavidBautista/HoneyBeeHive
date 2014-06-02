# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0009_post_response_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbee',
            name='default_language',
            field=models.CharField(default=b'en', max_length=10),
            preserve_default=True,
        ),
    ]
