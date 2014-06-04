# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0011_userstory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptanceCriteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_story', models.ForeignKey(to='bee.UserStory', to_field='id')),
                ('data', models.CharField(max_length=255)),
                ('expected_result', models.CharField(max_length=255)),
                ('expected_message', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='methodology',
            field=models.CharField(default='Scrum', max_length=32, choices=[('Scrum', 'Scrum'), ('Traditional', 'Traditional'), ('Kanvas', 'Kanvas')]),
            preserve_default=True,
        ),
    ]
