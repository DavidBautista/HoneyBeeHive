from django import forms
from bee.models import BeeTask, Project, UserStory, WORKERS_PERMISSIONS, UserBee, AssignedWorkerToProject
from django.utils.translation import ugettext_lazy as _


class Html5DateInput(forms.DateInput):
    input_type = 'date'

# name = models.CharField(max_length=140)
# ttype = models.CharField(max_length=64)
# description = models.CharField(max_length=1024)
# pred_start_date = models.DateTimeField(null=True)
# pred_end_date = models.DateTimeField(null=True)
# real_start_date = models.DateTimeField(null=True)
# real_end_date = models.DateTimeField(null=True)
# time_prevision = models.TimeField(null=True)
# parent_task = models.ForeignKey('BeeTask', related_name='child_tasks')
# sprint = models.ForeignKey('Sprint', related_name='ttasks')
# created_by = models.ForeignKey('UserBee', related_name='created_tasks')


#by instance: created_by, sprint_id
class TaskCreationForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ttype = forms.CharField(
        label=_("Type"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':6})
    )
    pred_start_date = forms.DateField(
        label=_('Start date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )
    pred_end_date = forms.DateField(
        label=_('End date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )
    time_prevision = forms.TimeField(
        label=_('Time prevision'),
        widget=forms.TimeInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BeeTask
        fields = ['name', 'ttype', 'description', 'pred_start_date', 'pred_end_date', 'time_prevision']

