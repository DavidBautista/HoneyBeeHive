from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.utils.translation import get_language
from django.views.decorators.cache import cache_page
from bee.models import UserBee
from bee.forms.auth_forms import RegisterForm, LoginForm
from HoneyBeeHive import settings


def register(request):
    if request.method == 'POST':
        new_user = UserBee(default_language=get_language())
        form = RegisterForm(request.POST, instance=new_user)
        if form.is_valid():
            new_user = form.save()
            if new_user is not None:
                return render_to_response(
                    "bee/auth/activate_email.html",
                    {},
                    context_instance=RequestContext(request))

    else:
        form = RegisterForm()
    return render_to_response(
        "bee/auth/register.html",
        {'register_form': form},
        context_instance=RequestContext(request))


@cache_page(60*15)
def register_colorbox(request):
    form = RegisterForm()
    return render_to_response(
        "bee/auth/_register_form.html",
        {'register_form': form},
        context_instance=RequestContext(request))


def activate(request):
    email = request.GET.get('email')
    code = request.GET.get('code')
    user = UserBee.objects.get(email=email)
    if email and code and not user.is_active:
        if UserBee.activate_user(email,  code):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect(reverse(settings.USER_INDEX))
        else:
            return HttpResponseForbidden()
    elif user.is_active:
        return HttpResponseRedirect(reverse(settings.USER_INDEX))
    else:
        return HttpResponse("Check your email")


def login_user(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login(request, login_form.cleaned_data['user'])
            return HttpResponseRedirect(reverse(settings.USER_INDEX))
    else:
        login_form = LoginForm()
    return render_to_response(
        "bee/auth/login.html",
        {'login_form': login_form},
        context_instance=RequestContext(request))


@cache_page(60*15)
def login_colorbox(request):
    login_form = LoginForm()
    return render_to_response(
        "bee/auth/_login_form.html",
        {'login_form': login_form},
        context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))