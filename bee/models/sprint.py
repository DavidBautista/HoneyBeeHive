from django.db import models
#from bee.models.project import Project


class Sprint(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    project = models.ForeignKey('Project', related_name='sprints')

    class Meta:
        app_label="bee"
