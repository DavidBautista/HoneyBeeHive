from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from project_management.forms.auth_forms import RegisterForm
from project_management.decorators.auth import anonymous_required

@anonymous_required
def index(request):
    form = RegisterForm()
    return render_to_response('templates/project_management/common/index.html',
        {'form': form, 'error': ""},
        context_instance=RequestContext(request))


def features(request):
    return render_to_response('templates/project_management/common/features.html',
        {},
        context_instance=RequestContext(request))


def pricing(request):
    return render_to_response('templates/project_management/common/pricing.html',
        {},
        context_instance=RequestContext(request))


def help_and_community(request):
    return render_to_response('templates/project_management/common/help_and_community.html',
        {},
        context_instance=RequestContext(request))


def about(request):
    return render_to_response('templates/project_management/common/about.html',
        {},
        context_instance=RequestContext(request))
