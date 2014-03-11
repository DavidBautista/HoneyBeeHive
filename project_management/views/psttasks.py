from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.views.decorators.http import require_POST, require_http_methods
from project_management.models import Project
from project_management.forms.psttask_forms import ProjectForm
import pprint
from django.contrib import messages


@login_required
def projects(request):
    pr_list = Project.objects.filter(created_by=request.user)
    return render_to_response('templates/project_management/psttasks/projects.html',
        {'projects': pr_list},
        context_instance=RequestContext(request))

@login_required
def project(request, proj_id):
    pr = Project.objects.get(id=proj_id)
    return render_to_response('templates/project_management/psttasks/project.html',
        {'project': pr},
        context_instance=RequestContext(request))



@login_required
# @require_http_methods(['POST, GET'])
def create_project(request):
    if request.method == 'POST':
        #Trying to create a new project
        new_project = Project(created_by=request.user)
        form = ProjectForm(request.POST, instance=new_project)
        if form.is_valid():
            #the project data is valid
            new_project = form.save()
            messages.success(request, "project created")
            return HttpResponseRedirect(reverse('project', kwargs={'proj_id': new_project.id}))
        #the project data is not valid
    else:
        #requesting the create project page
        form = ProjectForm()
    messages.success(request, "caca created")

    return render_to_response('templates/project_management/psttasks/create_project.html',
        {'form': form, 'user': request.user},
        context_instance=RequestContext(request))

