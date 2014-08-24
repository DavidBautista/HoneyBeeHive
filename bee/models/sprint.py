from django.db import models
from discussion import Discussion
from beetask import BeeTask

class Sprint(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    project = models.ForeignKey('Project', related_name='sprints')

    class Meta:
        app_label="bee"

    def start_date_f(self):
        return self.start_date.date()

    def end_date_f(self):
        return self.end_date.date()

    def num_discussions(self):
        return Discussion.objects.filter(sprint=self).count()

    def num_tasks(self):
        return BeeTask.objects.filter(sprint=self).count()

    def num_tasks_completed(self):
        return BeeTask.objects.filter(sprint=self, status=4).count()