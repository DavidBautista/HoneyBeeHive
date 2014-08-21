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
from standard import DateSerializer


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
        serializer = DateSerializer()
        fields = (
            'id',
            'name',
            'description',
            'pred_start_date',
            'pred_end_date',
            'time_prevision',
            'assigned_user',

        )
        filtering = {
            'sprint': ALL_WITH_RELATIONS
        }
    def dehydrate(self, bundle):
        bundle.data['username'] = bundle.obj.assigned_user.name

        return bundle

#todo darle formato a las fechas http://django-tastypie.readthedocs.org/en/latest/serialization.html#format-datetime