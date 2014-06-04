from django.db import models
from user_bee import UserBee

class UserStory(models.Model):
    why = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    what = models.CharField(max_length=255)
    owner = models.ForeignKey('UserBee')

    ## acceptance criterias

    class Meta:
        app_label = "bee"


