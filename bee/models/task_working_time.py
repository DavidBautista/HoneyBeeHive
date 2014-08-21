from django.db import models

class TaskWorkingTime(models.Model):
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    btask = models.ForeignKey('BeeTask', related_name='times_worked', null=True)

    class Meta:
        app_label = "bee"
