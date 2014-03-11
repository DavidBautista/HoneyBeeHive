from django.forms import ModelForm
from project_management.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'ptype', 'description', 'pred_start_date', 'pred_end_date']
