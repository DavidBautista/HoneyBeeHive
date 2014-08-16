from tastypie.authentication import SessionAuthentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from bee.models import UserBee, Project, Sprint, BeeTask
from django.utils.translation import ugettext as _, activate, deactivate
from standard import SimpleReaderAuthorization, ProjectReaderAuthorization
import tastypie.compat



class _SprintResource(ModelResource):
    class Meta:
        allowed_methods = ['get']
        queryset = Sprint.objects.all()
        authentication = SessionAuthentication()
        fields = (
            'id'
        )


class TaskResource(ModelResource):
    sprint = fields.ToOneField(_SprintResource, 'sprint', full=True)

    class Meta:
        allowed_methods = ['get']
        queryset = BeeTask.objects.all()
        authentication = SessionAuthentication()
        fields = (
            'id',
            'name',
            'description',
            'pred_start_date',
            'pred_end_date',
            'time_prevision',
            'created_by',

        )
        filtering = {
            'sprint': ALL_WITH_RELATIONS
        }

#todo darle formato a las fechas http://django-tastypie.readthedocs.org/en/latest/serialization.html#format-datetime