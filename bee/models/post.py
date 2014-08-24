from django.db import models
#from bee.models.user_bee import UserBee
#from bee.models.discussion import Discussion


class Post(models.Model):
    content = models.CharField(max_length=1024)
    sender = models.ForeignKey('UserBee', related_name='posts')
    discussion = models.ForeignKey('Discussion', related_name='posts')
    date = models.DateTimeField(auto_now_add=True, default=None)

    class Meta:
        app_label="bee"