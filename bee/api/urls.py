from tastypie.api import Api
import sprints_list
import tasks


api = Api(api_name='0.1.0')

api.register(sprints_list.SprintResource())
api.register(tasks.TaskResource())

from django.conf.urls import *

urlpatterns = patterns('',(r'^bee/', include(api.urls)))
