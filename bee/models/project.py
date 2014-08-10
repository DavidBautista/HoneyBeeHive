from django.db import models
#from bee.models.user_bee import UserBee
from _enums import PROJECT_METODOLOGES


class Project(models.Model):
    name = models.CharField(max_length=140)
    ptype = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    pred_start_date = models.DateTimeField(null=True)
    pred_end_date = models.DateTimeField(null=True)
    real_start_date = models.DateTimeField(null=True)
    real_end_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey('UserBee', related_name='created_projects')
    methodology = models.CharField(choices=PROJECT_METODOLOGES, max_length=32, default=PROJECT_METODOLOGES[0][0])

    class Meta:
        app_label="bee"