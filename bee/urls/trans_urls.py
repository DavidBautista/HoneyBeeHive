from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    #COMMON
    url(r'^features/$', 'bee.views.common.features', name='features'),
    url(r'^pricing/$', 'bee.views.common.pricing', name='pricing'),
    url(r'^help_and_community/$', 'bee.views.common.help_and_community', name='help_and_community'),
    url(r'^about/$', 'bee.views.common.about', name='about'),

    #AUTH
    url(r'^login/$', 'bee.views.auth.login_user', name='login'),
    url(r'^login_box/$', 'bee.views.auth.login_colorbox', name='login_box'),
    url(r'^register/$', 'bee.views.auth.register',  name='register'),
    url(r'^register_box/$', 'bee.views.auth.register_colorbox',  name='register_box'),
    url(r'^activate_email/$', 'bee.views.auth.activate', name='activate_email'),

    #PROJECTS
    url(r'^projects/$', 'bee.views.scrum_projects.projects', name='projects_list'),
    url(r'^create_project/$', 'bee.views.scrum_projects.create_project', name='create_project'),

    url(r'^project/(?P<proj_id>\d+)/$', 'bee.views.scrum_projects.project', name='project'),
    url(r'^project/(?P<proj_id>\d+)/user_stories/$', 'bee.views.scrum_projects.user_stories', name='user_stories'),
    url(r'^project/(?P<proj_id>\d+)/create_user_story/$', 'bee.views.scrum_projects.create_user_story', name='create_user_story'),
    url(r'^project/(?P<proj_id>\d+)/new_user_story/$', 'bee.views.scrum_projects.new_user_story', name='new_user_story'),

    url(r'^project/(?P<proj_id>\d+)/gantt_diagram/$', 'bee.views.scrum_projects.gantt_diagram', name='gantt_diagram'),


    url(r'^project/(?P<proj_id>\d+)/niko_calendar/$', 'bee.views.scrum_projects.niko_calendar', name='niko_calendar'),
    url(r'^project/(?P<proj_id>\d+)/admin_project/$', 'bee.views.scrum_projects.admin_project', name='admin_project'),
    url(r'^project/(?P<proj_id>\d+)/add_participant_to_project/$', 'bee.views.scrum_projects.add_participant_to_project', name='add_participant_to_project'),

    #SPRINTS & TASKS
    url(r'^project/(?P<proj_id>\d+)/create_sprint/cb/$', 'bee.views.scrum_projects.create_sprint_colorbox', name='create_sprint_colorbox'),
    url(r'^project/(?P<proj_id>\d+)/create_sprint_js/$', 'bee.views.scrum_projects.create_sprint_js', name='create_sprint_js'),

    url(r'^project/(?P<proj_id>\d+)/sprints/$', 'bee.views.scrum_projects.sprints', name='sprints'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/$', 'bee.views.scrum_sprints.sprint', name='sprint_overview'),

    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/tasks/$', 'bee.views.scrum_sprints.tasks', name='tasks'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/create_task_colorbox/$', 'bee.views.scrum_sprints.create_task_colorbox', name='create_task_colorbox'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/create_task_js/$', 'bee.views.scrum_sprints.create_task_js', name='create_task_js'),


    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/start_working/$', 'bee.views.scrum_sprints.work_in_task', name='work_in_task'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/pause/$', 'bee.views.scrum_sprints.pause_task', name='pause_task'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/complete/$', 'bee.views.scrum_sprints.complete_task', name='complete_task'),
    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/create_incidence/$', 'bee.views.scrum_sprints.create_incidence', name='create_incidence'),


    #PROFILE SUMMARY

    #MESSAGING & DISCUSSION
    url(r'^project/(?P<proj_id>\d+)/discussions/$', 'bee.views.discussions.project_discussions', name='project_discussions'),
    url(r'^project/(?P<proj_id>\d+)/discussion/(?P<dis_id>\d+)/$', 'bee.views.discussions.discussion_detail', name='discussion_detail'),
    url(r'^project/(?P<proj_id>\d+)/discussion/(?P<dis_id>\d+)/comment/$', 'bee.views.discussions.comment_in_discussion', name='comment_in_discussion'),

    url(r'^project/(?P<proj_id>\d+)/discussions_colorbox/$', 'bee.views.discussions.create_discussion_colorbox', name='create_project_discussion_colorbox'),
    url(r'^project/(?P<proj_id>\d+)/discussions_js/$', 'bee.views.discussions.create_discussion_js', name='create_project_discussion_js'),

    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/discussions/$', 'bee.views.discussions.sprint_discussions', name='sprint_discussions'),
    url(r'^project/(?P<proj_id>\d+)/(?P<spr_id>\d+)/discussions_colorbox/$', 'bee.views.discussions.create_discussion_colorbox', name='create_sprint_discussion_colorbox'),
    url(r'^project/(?P<proj_id>\d+)/sprint/(?P<spr_id>\d+)/discussions_js/$', 'bee.views.discussions.create_discussion_js', name='create_sprint_discussion_js'),

    url(r'^project/(?P<proj_id>\d+)/sprints/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/discussions/$', 'bee.views.discussions.task_discussions', name='task_discussions'),
    url(r'^project/(?P<proj_id>\d+)/(?P<spr_id>\d+)/(?P<task_id>\d+)/discussions_colorbox/$', 'bee.views.discussions.create_discussion_colorbox', name='create_task_discussion_colorbox'),
    url(r'^project/(?P<proj_id>\d+)/sprint/(?P<spr_id>\d+)/task/(?P<task_id>\d+)/discussions_js/$', 'bee.views.discussions.create_discussion_js', name='create_task_discussion_js'),
)