from django.db import models
from bee.models.user_bee import UserBee
from bee.models.discussion import Discussion
from bee.models.post import Post

class DiscussionSubscription(models.Model):
    user = models.ForeignKey('UserBee', related_name='subscribed_discussion')
    discussion = models.ForeignKey('Discussion', related_name='subscribed_users')
    last_read_post = models.ForeignKey('Post')
    new_messages = models.BooleanField(default=False)

    class Meta:
        app_label="bee"