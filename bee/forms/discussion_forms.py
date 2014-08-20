from django import forms
from bee.models import BeeTask, Project, UserStory, WORKERS_PERMISSIONS, UserBee, AssignedWorkerToProject
from django.utils.translation import ugettext_lazy as _
import datetime

class Html5DateInput(forms.DateInput):
    input_type = 'date'

valid_time_formats = ['%H:%M', '%H']

#by instance: created_by, sprint_id
class PostCommentForm(forms.ModelForm):
    content = forms.CharField(
        label=_('Content'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'max-length':1024}),
        required=False
    )

    class Meta:
        model = BeeTask
        fields = ['content']

