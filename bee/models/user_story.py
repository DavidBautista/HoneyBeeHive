from django.db import models
from user_bee import UserBee
from project import Project


class UserStory(models.Model):
    why = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    what = models.CharField(max_length=255)
    owner = models.ForeignKey('UserBee')
    project = models.ForeignKey('Project')
    ## acceptance criterias

    class Meta:
        app_label = "bee"


