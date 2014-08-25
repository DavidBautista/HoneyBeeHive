from django.db import models
#from user_story import UserStory


class AcceptanceCriteria(models.Model):
    user_story = models.ForeignKey('UserStory')
    data = models.CharField(max_length=255)
    expected_result = models.CharField(max_length=255)
    expected_message = models.CharField(max_length=255)