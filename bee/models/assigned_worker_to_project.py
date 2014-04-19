from django.db import models
from bee.models.user_bee import UserBee
from bee.models.project import Project

class AssignedWorkerToProject(models.Model):
    uworker = models.ForeignKey('UserBee', related_name='project_assigned')
    project = models.ForeignKey('Project', related_name='worker_assigned')
    role = models.CharField(max_length=64)

    class Meta:
        app_label="bee"