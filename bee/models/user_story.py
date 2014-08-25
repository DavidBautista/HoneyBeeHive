from django.db import models
from user_bee import UserBee
from project import Project
from user_story_acceptance_criteria import AcceptanceCriteria

class UserStory(models.Model):
    why = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    what = models.CharField(max_length=255)
    owner = models.ForeignKey('UserBee')
    project = models.ForeignKey('Project', related_name='user_story')
    ## acceptance criterias

    class Meta:
        app_label = "bee"

    def acceptance_criterias(self):
        return AcceptanceCriteria.objects.filter(user_story=self)
