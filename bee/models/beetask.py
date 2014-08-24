from django.db import models
#from bee.models.user_bee import UserBee
#from bee.models.sprint import Sprint
from bee.models.task_working_time import TaskWorkingTime
from _enums import TASKS_STATUS
import datetime

class BeeTask(models.Model):
    name = models.CharField(max_length=140)
    ttype = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    pred_start_date = models.DateField(null=True)
    pred_end_date = models.DateField(null=True)
    real_start_date = models.DateField(null=True)
    real_end_date = models.DateField(null=True)
    time_prevision = models.TimeField(null=True)
    time_worked = models.TimeField(null=True)
    sprint = models.ForeignKey('Sprint', related_name='ttasks')
    created_by = models.ForeignKey('UserBee', related_name='created_tasks')
    assigned_user = models.ForeignKey('UserBee', related_name='assigned_tasks', null=True, default=None)
    status = models.SmallIntegerField(choices=TASKS_STATUS, default=1)

    class Meta:
        app_label="bee"

    def update_time_worked(self):
        #todo sumar todas las diferencias de tiempo entre los TaskWorkingTime de la tarea

        twts = TaskWorkingTime.objects.filter(btask=self)
        timesum = datetime.timedelta(seconds=0)

        for twt in twts:
            timesum += (twt.end_date-twt.start_date)
        print timesum, timesum.seconds/3600, (timesum.seconds%3600)/60, timesum.seconds%60
        self.time_worked = datetime.time(hour=timesum.seconds/3600, minute=(timesum.seconds%3600)/60, second=timesum.seconds%60)
        self.save()