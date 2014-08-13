from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from bee.decorators.permissions import check_project_read_js, check_project_read, check_project_write, \
    check_project_write_js, check_project_admin_js, check_project_admin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from bee.models import Project, UserStory, Sprint, AssignedWorkerToProject
from bee.forms.sprints_forms import TaskCreationForm
import pprint
from django.contrib import messages
import json


@login_required
@check_project_read
def sprint(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=proj_id)

    return render_to_response('templates/bee/scrum_projects/sprints/overview.html',
        {'project': pr, 'sprint': spr},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def tasks(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=proj_id)

    return render_to_response('templates/bee/scrum_projects/sprints/tasks.html',
        {'project': pr, 'sprint': spr},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def create_task_colorbox(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=proj_id)
    task_form = TaskCreationForm()
    return render_to_response('templates/bee/scrum_projects/sprints/_task_creation_form.html',
        {'project': pr, 'sprint': spr, 'task_form': task_form},
        context_instance=RequestContext(request))

@login_required
@check_project_write
def create_task_js(request, proj_id, spr_id):
    pass