from bee.models import *
from tastypie.authorization import Authorization


class SimpleReaderAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.filter(user=bundle.request.user)


class ProjectReaderAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        #todo add participants
        return object_list.filter(created_by=bundle.request.user)