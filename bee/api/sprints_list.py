from tastypie.authentication import SessionAuthentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from bee.models import UserBee, Project, Sprint
from django.utils.translation import ugettext as _, activate, deactivate
from standard import SimpleReaderAuthorization, ProjectReaderAuthorization
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

    class Meta:
        allowed_methods = ['get']
        queryset = Sprint.objects.all()
        authentication = SessionAuthentication()
        fields = (
            'id',
            'name',
        )
        filtering = {
            'project': ALL_WITH_RELATIONS
        }

#todo darle formato a las fechas http://django-tastypie.readthedocs.org/en/latest/serialization.html#format-datetime