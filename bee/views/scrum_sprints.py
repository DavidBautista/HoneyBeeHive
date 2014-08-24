from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from bee.decorators.permissions import check_project_read_js, check_project_read, check_project_write, \
    check_project_write_js, check_project_admin_js, check_project_admin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from bee.models import Project, UserStory, Sprint, AssignedWorkerToProject, BeeTask, TaskWorkingTime, UserBee, Discussion
from bee.models._enums import TASKS_STATUS
from bee.forms.sprints_forms import TaskCreationForm
import pprint
from django.contrib import messages
import json
import datetime

@login_required
@check_project_read
def sprint(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    numtasks = BeeTask.objects.filter(sprint=spr).count()
    btasks = BeeTask.objects.filter(sprint=spr, status=4).order_by('real_end_date')
    counter = numtasks
    ini_date = spr.start_date.date()
    counts_array = []
    for btask in btasks:
        if btask.real_end_date > ini_date:
            counts_array.append((ini_date, counter))
            ini_date+=datetime.timedelta(days=1)
        counter-=1

    counts_array.append((ini_date, counter))
    discussion_list = Discussion.objects.filter(sprint=spr).order_by('-start_date')[0:3]
    return render_to_response('bee/scrum_projects/sprints/overview.html',
        {'project': pr, 'sprint': spr, 'numtasks':numtasks, 'tasks':reversed(list(btasks)[-5:]),
         'completed_tasks': counts_array, 'completed_tasks_count': btasks.__len__(),'discussion_list': discussion_list },
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
    project_participants = UserBee.objects.raw('SELECT ub.* FROM bee_userbee as ub LEFT JOIN bee_assignedworkertoproject as ad ON ub.id=ad.uworker_id WHERE ad.project_id=%s', [proj_id])
    return render_to_response('bee/scrum_projects/sprints/_task_creation_form.html',
        {'project': pr, 'sprint': spr, 'task_form': task_form, 'project_participants': project_participants},
        context_instance=RequestContext(request))

@login_required
@check_project_write
def create_task_js(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    reset_dom = 'true' if spr.ttasks.count() == 0 else 'false'
    try:
        user_assign = UserBee.objects.get(id=request.POST.get('user_assign'))
    except UserBee.DoesNotExist as e:
        print e.message
        return render_to_response('bee/scrum_projects/sprints/_create_task_error.js',
                {'project': pr, 'sprint': spr, 'task_form': TaskCreationForm(request.POST)}, content_type='text/x-javascript',
                context_instance=RequestContext(request))
    taskObj = BeeTask(sprint=spr, created_by=request.user, assigned_user=user_assign)
    task_form = TaskCreationForm(request.POST, instance=taskObj)
    if task_form.is_valid():
        new_task = task_form.save()
        return render_to_response('bee/scrum_projects/sprints/_create_task.js',
            {'project': pr, 'sprint': spr, 'new_task': new_task, 'reset_dom':reset_dom}, content_type='text/x-javascript',
            context_instance=RequestContext(request))
    else:
        return render_to_response('bee/scrum_projects/sprints/_create_task_error.js',
                {'project': pr, 'sprint': spr, 'task_form':task_form}, content_type='text/x-javascript',
                context_instance=RequestContext(request))


def work_in_task(request, proj_id, spr_id, task_id):
    task = BeeTask.objects.get(id=task_id)
    error = ''
    if request.user == task.assigned_user:
        if task.status in [1, 3]:
            if task.status == 1:
                task.real_start_date = datetime.date.today()
            task.status = 2
            twt = TaskWorkingTime(start_date=datetime.datetime.now(), btask=task)
            task.save()
            twt.save()
        else:
            error = '?error=1'
    else:
        error = '?error=2'
    return HttpResponseRedirect(reverse('tasks', kwargs={'proj_id': proj_id, 'spr_id': spr_id})+error)


def pause_task(request, proj_id, spr_id, task_id):
    task = BeeTask.objects.get(id=task_id)
    error = ''
    if request.user == task.assigned_user:
        if task.status == 2:
            now = datetime.datetime.now()
            task.status = 3
            twt = TaskWorkingTime.objects.get(btask=task, end_date=None)
            twt.end_date = now
            task.save()
            twt.save()
        else:
            error = '?error=3'
    else:
        error = '?error=4'

    return HttpResponseRedirect(reverse('tasks', kwargs={'proj_id': proj_id, 'spr_id': spr_id})+error)



def complete_task(request, proj_id, spr_id, task_id):
    task = BeeTask.objects.get(id=task_id)
    error = ''
    if request.user == task.assigned_user:
        if task.status in [2,3]:
            now = datetime.datetime.now()
            task.status = 4
            try:
                twt = TaskWorkingTime.objects.get(btask=task, end_date=None)
                twt.end_date = now
                twt.save()
            except TaskWorkingTime.DoesNotExist as e:
                pass
            task.real_end_date = now
            task.update_time_worked()
            task.save()
        else:
            error = '?error=3'
    else:
        error = '?error=4'

    return HttpResponseRedirect(reverse('tasks', kwargs={'proj_id': proj_id, 'spr_id': spr_id})+error)

def create_incidence(request, proj_id, spr_id, task_id):
    pass