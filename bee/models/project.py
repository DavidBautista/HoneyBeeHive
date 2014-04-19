from django.db import models
from user_bee import UserBee

class Project(models.Model):
    name = models.CharField(max_length=140)
    ptype = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    pred_start_date = models.DateTimeField(null=True)
    pred_end_date = models.DateTimeField(null=True)
    real_start_date = models.DateTimeField(null=True)
    real_end_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey('UserBee', related_name='created_projects')

    class Meta:
        app_label="bee"