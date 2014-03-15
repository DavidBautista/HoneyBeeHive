from django import forms
from project_management.models import Project
from django.utils.translation import ugettext_lazy as _


class Html5DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Project name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ptype = forms.CharField(
        label=_("Project type"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    pred_start_date = forms.DateField(
        label=_('Start date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )
    pred_end_date = forms.DateField(
        label=_('End date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Project
        fields = ['name', 'ptype', 'description', 'pred_start_date', 'pred_end_date']
