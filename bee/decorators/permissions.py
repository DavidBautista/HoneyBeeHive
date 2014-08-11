from django.utils.functional import wraps
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render_to_response
from bee.models import Project
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test, available_attrs
from django.core.exceptions import PermissionDenied


def check_project_admin_js(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_admin_permission(pr):
            return render_to_response('templates/bee/common/_permission_error.js',
                        {'project': pr}, content_type='text/x-javascript',
                        context_instance=RequestContext(request))
        return view(request, proj_id, *args, **kwargs)
    return inner


def check_project_write_js(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_write_permission(pr):
            return render_to_response('templates/bee/common/_permission_error.js',
                        {'project': pr}, content_type='text/x-javascript',
                        context_instance=RequestContext(request))
        return view(request, proj_id, *args, **kwargs)
    return inner


def check_project_read_js(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_read_permission(pr):
            return HttpResponseForbidden()
        return view(request, proj_id, *args, **kwargs)
    return inner


def check_project_admin(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_admin_permission(pr):
            return HttpResponseForbidden()
        return view(request, proj_id, *args, **kwargs)
    return inner


def check_project_write(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_write_permission(pr):
            return HttpResponseForbidden()
        return view(request, proj_id, *args, **kwargs)
    return inner


def check_project_read(view):
    @wraps(view)
    def inner(request, proj_id, *args, **kwargs):
        pr = Project.objects.get(id=proj_id)
        if not request.user.has_read_permission(pr):
            return HttpResponseForbidden()
        return view(request, proj_id, *args, **kwargs)
    return inner