from tastypie.authentication import SessionAuthentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from bee.models import UserBee, Project, Sprint
from django.utils.translation import ugettext as _, activate, deactivate
from standard import SimpleReaderAuthorization, ProjectReaderAuthorization, DateSerializer
import tastypie.compat


class _ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        authorization = ProjectReaderAuthorization()
        fields = (
            'id',
        )
        filter = (
            'id',
        )
        include_resource_uri = False


class SprintResource(ModelResource):
    project = user = fields.ToOneField(_ProjectResource, 'project', full=True)

    start_date_f = fields.CharField(attribute='start_date_f', readonly=True)
    end_date_f = fields.CharField(attribute='end_date_f', readonly=True)
    num_discussions = fields.IntegerField(attribute='num_discussions', readonly=True)
    num_tasks = fields.CharField(attribute='num_tasks', readonly=True)
    num_tasks_completed = fields.CharField(attribute='num_tasks_completed', readonly=True)

    class Meta:
        allowed_methods = ['get']
        queryset = Sprint.objects.all()
        authentication = SessionAuthentication()
        serializer = DateSerializer()
        fields = (
            'id',
            'name',
            'start_date_f',
            'end_date_f',
            'num_discussions',
            'num_tasks',
            'num_tasks_completed'
        )
        filtering = {
            'project': ALL_WITH_RELATIONS
        }


#todo authorization
#todo darle formato a las fechas http://django-tastypie.readthedocs.org/en/latest/serialization.html#format-datetime