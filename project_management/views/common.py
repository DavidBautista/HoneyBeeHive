from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from project_management.forms.auth_forms import register_form


def index(request):
    form = register_form()
    return render_to_response('templates/project_management/common/index.html',
        {'form':form, 'error':""},
      context_instance=RequestContext(request))