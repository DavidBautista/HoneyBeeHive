from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from bee.forms.auth_forms import RegisterForm, LoginForm
from bee.decorators.auth import anonymous_required

@anonymous_required
def index(request):
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_to_response('templates/bee/common/index.html',
        {'register_form': register_form, 'login_form': login_form},
        context_instance=RequestContext(request))


def features(request):
    return render_to_response('templates/bee/common/features.html',
        {},
        context_instance=RequestContext(request))


def pricing(request):
    return render_to_response('templates/bee/common/pricing.html',
        {},
        context_instance=RequestContext(request))


def help_and_community(request):
    return render_to_response('templates/bee/common/help_and_community.html',
        {},
        context_instance=RequestContext(request))


def about(request):
    return render_to_response('templates/bee/common/about.html',
        {},
        context_instance=RequestContext(request))
