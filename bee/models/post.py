from django.db import models
from bee.models.user_bee import UserBee
from bee.models.discussion import Discussion


class Post(models.Model):
    subject = models.CharField(max_length=140)
    content = models.CharField(max_length=1024)
    sender = models.ForeignKey('UserBee', related_name='posts')
    discussion = models.ForeignKey('Discussion', related_name='posts')
    response_to = models.ForeignKey('Post', related_name='responses', null=True)

    class Meta:
        app_label="bee"