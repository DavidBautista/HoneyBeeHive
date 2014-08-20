from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from bee.decorators.permissions import check_project_read_js, check_project_read, check_project_write, \
    check_project_write_js, check_project_admin_js, check_project_admin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from bee.models import Project, UserStory, Sprint, AssignedWorkerToProject, BeeTask
from bee.forms.sprints_forms import TaskCreationForm
import pprint
from django.contrib import messages
import json


@login_required
@check_project_read
def sprint(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)

    return render_to_response('bee/scrum_projects/sprints/overview.html',
        {'project': pr, 'sprint': spr},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def tasks(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)

    return render_to_response('bee/scrum_projects/sprints/tasks.html',
        {'project': pr, 'sprint': spr},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def create_task_colorbox(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    task_form = TaskCreationForm()
    return render_to_response('bee/scrum_projects/sprints/_task_creation_form.html',
        {'project': pr, 'sprint': spr, 'task_form': task_form},
        context_instance=RequestContext(request))

@login_required
@check_project_write
def create_task_js(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    reset_dom = 'true' if spr.ttasks.count() == 0 else 'false'
    taskObj = BeeTask(sprint=spr, created_by=request.user)
    task_form = TaskCreationForm(request.POST, instance=taskObj)
    if task_form.is_valid():
        new_task = task_form.save()
        return render_to_response('bee/scrum_projects/sprints/_create_task.js',
            {'project': pr, 'sprint': spr, 'new_task': new_task, 'reset_dom':reset_dom}, content_type='text/x-javascript',
            context_instance=RequestContext(request))
    else:
        task_form.save()
        print task_form.non_field_errors()
        return render_to_response('bee/scrum_projects/sprints/_create_task_error.js',
                {'project': pr, 'sprint': spr, 'task_form':task_form}, content_type='text/x-javascript',
                context_instance=RequestContext(request))
