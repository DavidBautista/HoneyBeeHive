from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import datetime

def __getitem__(self, item):
  return getattr(self,item)
def __setitem__(self, key, value):
  return setattr(self,key,value)
models.Model.__getitem__=__getitem__
models.Model.__setitem__=__setitem__


#####################################################################################
#####################################################################################
###############            MODEL MANAGERS                   #########################
#####################################################################################
#####################################################################################

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email="default@default.com", password="admin", **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_active = True
        u.is_superuser = True
        u.is_staff = True
        u.save(using=self._db)
        return u

#####################################################################################
#####################################################################################
###############                  MODELS                     #########################
#####################################################################################
#####################################################################################


class UserWorker(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    #from AbstractBaseUser
    #password = models.CharField(_('password'), max_length=128)
    #last_login = models.DateTimeField(_('last login'), default=timezone.now)
    #from PermissionsMixin
    #is_superuser = models.BooleanField(_('superuser status'),
    #                   default=False, help_text=_('Designates that this user has
    #                                             all permissions without explicitly assigning them.'))
    #groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True,
    #                                help_text=_('The groups this user belongs to. A user will get
    #                                          all permissions granted to each of his/her group.'))
    #user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'),
    #                                               blank=True,help_text='Specific permissions for this user.')

    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateField()

    email_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    ############### APP attributes ###############

    ############### PROPERTIES ###############
    def _get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def _get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    full_name = property(_get_full_name)
    short_name = property(_get_short_name)

    ############### METHODS ###############
    def __unicode__(self):
        return self.full_name


class Project(models.Model):
    name = models.CharField(max_length=140)
    ptype = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    pred_start_date = models.DateTimeField(null=True)
    pred_end_date = models.DateTimeField(null=True)
    real_start_date = models.DateTimeField(null=True)
    real_end_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(UserWorker, related_name='created_projects')


class Sprint(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    project = models.ForeignKey(Project, related_name='sprints')


class Ttask(models.Model):
    name = models.CharField(max_length=140)
    ttype = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    pred_start_date = models.DateTimeField(null=True)
    pred_end_date = models.DateTimeField(null=True)
    real_start_date = models.DateTimeField(null=True)
    real_end_date = models.DateTimeField(null=True)
    parent_task = models.ForeignKey('Ttask', related_name='child_tasks')
    sprint = models.ForeignKey(Sprint, related_name='ttasks')
    created_by = models.ForeignKey(UserWorker, related_name='created_tasks')


SCORE_CHOICES = zip(range(1, 10), range(1, 10))


class Issue(models.Model): #TODO pensar si es buen nombre
    seriousness = models.IntegerField(choices=SCORE_CHOICES, default=1)
    name = models.CharField(max_length=140)
    itype = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    time_effect = models.DateTimeField(null=True)
    ttask = models.ForeignKey(Ttask, related_name='issues')


class Discussion(models.Model):
    subject = models.CharField(max_length=140)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    project = models.ForeignKey(Project, related_name='discussions')
    sprint = models.ForeignKey(Sprint, related_name='discussions', null=True)
    task = models.ForeignKey(Ttask, related_name='discussions', null=True)
    started_by = models.ForeignKey(UserWorker, related_name='created_discussions')


class Post(models.Model):
    subject = models.CharField(max_length=140)
    content = models.CharField(max_length=1024)
    sender = models.ForeignKey(UserWorker, related_name='posts')
    discussion = models.ForeignKey(Discussion, related_name='posts')
    response_to = models.ForeignKey('Post', related_name='responses', null=True)


class DiscussionSubscription(models.Model):
    user = models.ForeignKey(UserWorker, related_name='subscribed_discussion')
    discussion = models.ForeignKey(Discussion, related_name='subscribed_users')
    last_read_post = models.ForeignKey(Post)
    new_messages = models.BooleanField(default=False)


class AssignedWorkerToTask(models.Model):
    uworker = models.ForeignKey(UserWorker, related_name='task_assigned')
    ttask = models.ForeignKey(Ttask, related_name='worker_assigned')
    role = models.CharField(max_length=64)

class AssignedWorkerToProject(models.Model):
    uworker = models.ForeignKey(UserWorker, related_name='project_assigned')
    project = models.ForeignKey(Project, related_name='worker_assigned')
    role = models.CharField(max_length=64)


