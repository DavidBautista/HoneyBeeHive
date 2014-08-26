from django.db import models

from bee.models.user_bee import UserBee
from bee.models.project import Project
from bee.models.sprint import Sprint
from bee.models.beetask import BeeTask
from bee.models.task_working_time import TaskWorkingTime
from bee.models.issue import Issue
from bee.models.discussion import Discussion
from bee.models.post import Post
from bee.models.assigned_worker_to_project import AssignedWorkerToProject
from bee.models.user_story import UserStory
from bee.models.user_story_acceptance_criteria import AcceptanceCriteria
from bee.models.nikoMood import NikoMood
from _enums import *

def __getitem__(self, item):
    return getattr(self, item)
def __setitem__(self, key, value):
    return setattr(self, key, value)
models.Model.__getitem__=__getitem__
models.Model.__setitem__=__setitem__


__all__ = ['UserBee', 'Project', 'Sprint', 'BeeTask', 'Issue', 'Discussion', 'Post',
           'TaskWorkingTime', 'AssignedWorkerToProject', 'NikoMood']
