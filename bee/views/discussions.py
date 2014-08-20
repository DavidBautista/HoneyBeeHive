from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from bee.decorators.permissions import check_project_read_js, check_project_read, check_project_write, \
    check_project_write_js, check_project_admin_js, check_project_admin
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from bee.models import Project, UserStory, Sprint, AssignedWorkerToProject, BeeTask, Discussion, Post
from bee.forms.discussion_forms import PostCommentForm
import pprint
from django.contrib import messages
import json

@login_required
@check_project_read
def project_discussions(request, proj_id):
    pr = Project.objects.get(id=proj_id)
    discussions = Discussion.objects.filter(project=pr).order_by('-id')

    return render_to_response('bee/scrum_projects/discussions.html',
        {'project': pr, 'discussion_list': discussions },
        context_instance=RequestContext(request))

@login_required
@check_project_read
def sprint_discussions(request, proj_id, spr_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    discussions = Discussion.objects.filter(project=pr, sprint=spr).order_by('-id')

    return render_to_response('bee/scrum_projects/sprints/discussions.html',
        {'project': pr, 'sprint': spr, 'discussion_list': discussions},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def task_discussions(request, proj_id, spr_id, task_id):
    pr = Project.objects.get(id=proj_id)
    spr = Sprint.objects.get(id=spr_id)
    task = BeeTask.objects.get(id=task_id)
    discussions = Discussion.objects.filter(project=pr, sprint=spr, task=task).order_by('-id')
    return render_to_response('bee/scrum_projects/sprints/tasks/discussions.html',
        {'project': pr, 'sprint': spr, 'task': task, 'discussion_list': discussions},
        context_instance=RequestContext(request))

@login_required
@check_project_read
def discussion_detail(request, proj_id, dis_id):
    pr = Project.objects.get(id=proj_id)
    dis = Discussion.objects.get(id=dis_id)
    post_list = Post.objects.filter(discussion_id=dis.id).order_by('id')
    comment_form = PostCommentForm()
    return render_to_response('bee/discussions/discussion_detail.html',
        {'project': pr, 'discussion': dis, 'post_list': post_list, 'comment_form': comment_form},
        context_instance=RequestContext(request))


@login_required
@check_project_read_js
def comment_in_discussion(request, proj_id, dis_id):
    pr = Project.objects.get(id=proj_id)
    dis = Discussion.objects.get(id=dis_id)
    new_post = Post(discussion=dis, sender=request.user)
    post_form = PostCommentForm(request.POST, instance=new_post)
    new_post = post_form.save()

    return render_to_response('bee/discussions/_comment_in_discussion.js',
            {'new_post': new_post}, content_type='text/x-javascript',
            context_instance=RequestContext(request))


@login_required
@check_project_read
def create_discussion_colorbox(request, proj_id, spr_id=None, task_id=None):
    pr = Project.objects.get(id=proj_id)
    response_dict = {'project': pr}
    if spr_id:
        spr = Sprint.objects.get(id=spr_id)
        response_dict['sprint'] = spr

        if task_id:
            task = BeeTask.objects.get(id=task_id)
            response_dict['task'] = task

    return render_to_response('bee/discussions/_discussion_creation_form.html',
        response_dict,
        context_instance=RequestContext(request))

@login_required
@check_project_read_js
def create_discussion_js(request, proj_id, spr_id=None, task_id=None):
    pr = Project.objects.get(id=proj_id)
    new_discussion = Discussion(project=pr, started_by=request.user, subject=request.POST.get('subject'))
    print spr_id
    if spr_id:
        spr = Sprint.objects.get(id=spr_id)
        new_discussion.sprint = spr
        if task_id:
            task = BeeTask.objects.get(id=task_id)
            new_discussion.task = task
    new_discussion.save()
    new_post = Post(sender=request.user, content=request.POST.get('content'), discussion=new_discussion)
    new_post.save()

    return render_to_response('bee/discussions/_create_discussion.js',
            {'new_discussion': new_discussion, 'new_post':new_post}, content_type='text/x-javascript',
            context_instance=RequestContext(request))

