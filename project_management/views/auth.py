from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from project_management.models import UserWorker
from project_management.forms.auth_forms import RegisterForm
from project_management.forms.auth_validation import activate_user, send_activation_mail


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print "FORM VALID"
            new_user = form.save()
            user = authenticate(email=request.POST.get('email'),
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
        form = RegisterForm()
        return render_to_response(
            "templates/project_management/auth/register.html",
            {'form': form},
            context_instance=RequestContext(request))


def activate(request):
    email = request.GET.get('email')
    code = request.GET.get('code')
    user = UserWorker.objects.get(email=email)
    if email and code and not user.is_active:
        if activate_user(email,  code):
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect("/profile/")
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponse("Check your email")


def login_user(request):
    #TODO tener en cuenta el "remember me"
    error = ""
    if request.method == "POST":
        user = authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/profile/")
            #TODO add celery task with the activation email
            #send_activation_mail(user)
            error = "Check your email for an activation link."
        else:
            error = "Incorrect email or password."
    return render_to_response(
        "templates/project_management/auth/login.html",
        {'error': error},
        context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return redirect("/")