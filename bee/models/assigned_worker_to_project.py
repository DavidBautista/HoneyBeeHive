from django.db import models
#from bee.models.user_bee import UserBee
#from bee.models.project import Project
from _enums import WORKERS_PERMISSIONS

class AssignedWorkerToProject(models.Model):
    uworker = models.ForeignKey('UserBee', related_name='project_assigned')
    project = models.ForeignKey('Project', related_name='worker_assigned')
    role = models.CharField(max_length=64)
    permissions = models.SmallIntegerField(choices=WORKERS_PERMISSIONS, default=1)

    def get_permission_level(self):
        return WORKERS_PERMISSIONS[self.permissions-1][1]

    permission_level = property(get_permission_level)

    class Meta:
        app_label="bee"