from django.db import models
from bee.models.user_bee import UserBee
from bee.models.beetask import BeeTask

class AssignedWorkerToTask(models.Model):
    uworker = models.ForeignKey('UserBee', related_name='task_assigned')
    ttask = models.ForeignKey('BeeTask', related_name='worker_assigned')
    role = models.CharField(max_length=64)

    class Meta:
        app_label="bee"