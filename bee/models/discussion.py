from django.db import models
import datetime
from bee.models.user_bee import UserBee
from bee.models.project import Project
from bee.models.sprint import Sprint
from bee.models.beetask import BeeTask

class Discussion(models.Model):
    subject = models.CharField(max_length=140)
    start_date = models.DateTimeField(default=datetime.datetime.now()) #todo utc
    project = models.ForeignKey('Project', related_name='discussions')
    sprint = models.ForeignKey('Sprint', related_name='discussions', null=True)
    task = models.ForeignKey('BeeTask', related_name='discussions', null=True)
    started_by = models.ForeignKey('UserBee', related_name='created_discussions')

    class Meta:
        app_label="bee"