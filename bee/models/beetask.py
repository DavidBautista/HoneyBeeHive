from django.db import models
from bee.models.user_bee import UserBee
from bee.models.sprint import Sprint

class BeeTask(models.Model):
    name = models.CharField(max_length=140)
    ttype = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    pred_start_date = models.DateTimeField(null=True)
    pred_end_date = models.DateTimeField(null=True)
    real_start_date = models.DateTimeField(null=True)
    real_end_date = models.DateTimeField(null=True)
    time_prevision = models.TimeField(null=True)
    parent_task = models.ForeignKey('BeeTask', related_name='child_tasks')
    sprint = models.ForeignKey('Sprint', related_name='ttasks')
    created_by = models.ForeignKey('UserBee', related_name='created_tasks')

    class Meta:
        app_label="bee"