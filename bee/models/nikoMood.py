from django.db import models
from _enums import NIKO_CHOICES


class NikoMood(models.Model):
    project = models.ForeignKey('Project', related_name='niko_moods_users')
    user = models.ForeignKey('UserBee', related_name='niko_moods_projects')
    mood = models.SmallIntegerField(choices=NIKO_CHOICES, default=2)
    date = models.DateField(auto_now_add=True)

    class Meta:
        app_label="bee"