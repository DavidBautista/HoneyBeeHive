from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from bee.decorators.permissions import check_project_read_js, check_project_read, check_project_write, \
    check_project_write_js, check_project_admin_js, check_project_admin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from bee.models import Project, UserStory, Sprint, AssignedWorkerToProject, BeeTask
from bee.forms.projects_forms import ProjectForm, UserStoryForm, SprintForm, AddParticipantToProjectForm
import pprint
from django.contrib import messages
import json


def project_discussions(request, proj_id):
    pr = Project.objects.get(id=proj_id)
    return render_to_response('bee/scrum_projects/discussions.html',
        {'project': pr},
        context_instance=RequestContext(request))


def sprint_discussions(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    return render_to_response('bee/scrum_projects/sprints/discussions.html',
        {'project': pr, 'sprint': spr},
        context_instance=RequestContext(request))


def task_discussions(request, proj_id, spr_id, task_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    task = BeeTask.objects.get(id=task_id)
    return render_to_response('bee/scrum_projects/sprints/tasks/discussions.html',
        {'project': pr, 'sprint': spr, 'task': task},
        context_instance=RequestContext(request))

