from bee.models import *
from tastypie.authorization import Authorization
from django.utils import formats
from tastypie.serializers import Serializer


class SimpleReaderAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)


class ProjectReaderAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        #todo add participants
        return object_list.filter(created_by=bundle.request.user)


class DateSerializer(Serializer):
    def format_datetime(self, data):
        return formats.date_format(data, "SHORT_DATETIME_FORMAT")
    def format_date(self, data):
        return formats.date_format(data, "SHORT_DATE_FORMAT")

