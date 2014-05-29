from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import datetime


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


class UserBee(AbstractBaseUser, PermissionsMixin):
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


    class Meta:
        app_label="bee"


    ############### PROPERTIES ###############
    def _get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    full_name = property(_get_full_name)
    short_name = property(get_short_name)

    ############### METHODS ###############
    def __unicode__(self):
        return self.full_name
