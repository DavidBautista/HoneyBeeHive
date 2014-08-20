from django.db import models
import datetime
from bee.models.user_bee import UserBee
from bee.models.project import Project
from bee.models.sprint import Sprint
from bee.models.beetask import BeeTask
from bee.models.post import Post

class Discussion(models.Model):
    subject = models.CharField(max_length=140)
    start_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', related_name='discussions')
    sprint = models.ForeignKey('Sprint', related_name='discussions', null=True)
    task = models.ForeignKey('BeeTask', related_name='discussions', null=True)
    started_by = models.ForeignKey('UserBee', related_name='created_discussions')

    def first_post(self):
        return Post.objects.filter(discussion=self).order_by('id')[0]


    class Meta:
        app_label="bee"