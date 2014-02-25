from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from project_management.forms.auth_forms import RegisterForm


def index(request):
    form = RegisterForm()
    return render_to_response('templates/project_management/common/index.html',
        {'form':form, 'error':""},
      context_instance=RequestContext(request))