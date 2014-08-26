from django.db import models
from _enums import SCORE_CHOICES
from bee.models.beetask import BeeTask

class Issue(models.Model):
    #seriousness = models.SmallIntegerField(choices=SCORE_CHOICES, default=1)
    #name = models.CharField(max_length=140)
    #itype = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    #time_effect = models.DateTimeField(null=True)
    ttask = models.ForeignKey('BeeTask', related_name='issues')

    class Meta:
        app_label="bee"