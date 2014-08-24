from django import forms
from bee.models import BeeTask, Project, UserStory, WORKERS_PERMISSIONS, UserBee, AssignedWorkerToProject
from django.utils.translation import ugettext_lazy as _
import datetime

class Html5DateInput(forms.DateInput):
    input_type = 'date'

valid_time_formats = ['%H:%M', '%H']

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
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        required=False
    )
    pred_start_date = forms.DateField(
        label=_('Start date'),
        widget=Html5DateInput(attrs={'class': 'form-control', 'value': datetime.date.today()})
    )
    pred_end_date = forms.DateField(
        label=_('End date'),
        widget=Html5DateInput(attrs={'class': 'form-control', 'value': datetime.date.today()+datetime.timedelta(days=1)})
    )
    time_prevision = forms.TimeField(
        label=_('Time prevision (hours)'),
        widget=forms.widgets.TimeInput(attrs={'class': 'form-control', 'value': '1:30'},),
        input_formats=valid_time_formats
    )

    def clean(self):
        if self.cleaned_data["pred_end_date"]< self.cleaned_data["pred_start_date"]:
            raise forms.ValidationError(_("End date cannot be before than start date."))
        else:
            return self.cleaned_data

    class Meta:
        model = BeeTask
        fields = ['name', 'ttype', 'description', 'pred_start_date', 'pred_end_date', 'time_prevision']

