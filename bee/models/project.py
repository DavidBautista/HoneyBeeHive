from django.db import models
from beetask import BeeTask
from discussion import Discussion
from assigned_worker_to_project import AssignedWorkerToProject
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

    def num_participants(self):

        return AssignedWorkerToProject.objects.filter(project=self).count()

    def num_tasks(self):
        return BeeTask.objects.filter(sprint__project=self).count()

    def num_completed_tasks(self):
        return BeeTask.objects.filter(sprint__project=self, status=4).count()

    def num_discussions(self):

        return Discussion.objects.filter(project=self).count()