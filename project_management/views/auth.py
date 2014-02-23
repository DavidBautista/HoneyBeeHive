from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from project_management.models import UserWorker
from project_management.forms.auth_forms import register_form
from project_management.forms.auth_validation import activate_user


def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=request.POST.get('username'),
                                password=request.POST.get('password1'))
            user.save()

            if user is not None:
                return render_to_response(
                    "templates/project_management/auth/activate_email.html",
                    {},
                    context_instance=RequestContext(request))
        return render_to_response(
            "templates/project_management/auth/register.html",
            {'form': form},
            context_instance=RequestContext(request))
    else:
        form = register_form()
        return render_to_response(
            "templates/project_management/auth/register.html",
            {'form': form},
            context_instance=RequestContext(request))


def activate(request):
    username = request.GET.get('username')
    code = request.GET.get('code')
    user = UserWorker.objects.get(username=username)
    if username and code and not user.is_active:
        if activate_user(username,  code):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect("/profile/")
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponse("Check your email")


def login_user(request):
    error = ""
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/profile/")
            error = "You don't have password."
        else:
            error = "Incorrect username or password."
    return render_to_response(
        "templates/project_management/auth/login.html",
        {'error': error},
        context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect("/")