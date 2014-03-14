from django import forms
from django.forms.widgets import Input
from django.forms.extras.widgets import SelectDateWidget
from project_management.models import Project



class Html5DateInput(forms.DateInput):
    input_type = 'date'
#
# class DateInput(Input):
#     input_type = 'date'
#
#
#     def __init__(self, attrs=None):
#         super(DateInput, self).__init__()
#         if attrs is not None:
#             self.input_type = attrs.pop('type', self.input_type)
#

class ProjectForm(forms.ModelForm):
    name = forms.CharField(label="Project name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    ptype = forms.CharField(label="Project type", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget= forms.Textarea(attrs={'class': 'form-control'}) )
    pred_start_date = forms.DateField(label='Start date', widget= Html5DateInput(attrs={'class': 'form-control'}))
    pred_end_date = forms.DateField(label='End date', widget= Html5DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        fields = ['name', 'ptype', 'description', 'pred_start_date', 'pred_end_date']
