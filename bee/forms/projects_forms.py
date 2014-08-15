from django import forms
from bee.models import Project, UserStory, WORKERS_PERMISSIONS, UserBee, AssignedWorkerToProject
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


class UserStoryForm(forms.ModelForm):
    why = forms.CharField(
        label=_("So that I can"),
        widget=forms.Textarea(attrs={'placeholder': _("achieve some goal"),
                                     'class': 'form-control user-story mb15', 'rows': '3', 'maxlength': '220'}),
        help_text=_("")
    )
    who = forms.CharField(
        label=_("As a"),
        widget=forms.Textarea(attrs={'placeholder': _("type of user"),
                                     'class': 'form-control user-story mb15', 'rows': '3', 'maxlength': '220'}),
        help_text=_("")
    )
    what = forms.CharField(
        label=_("I want"),
        widget=forms.Textarea(attrs={'placeholder': _("to perform some task"),
                                     'class': 'form-control user-story mb15', 'rows': '3', 'maxlength': '220'}),
        help_text=_("")
    )

    class Meta:
        model = Project
        fields = ['why', 'who', 'what', ]


class SprintForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Sprint name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    start_date = forms.DateField(
        label=_('Start date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )
    end_date = forms.DateField(
        label=_('End date'),
        widget=Html5DateInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date']


class AddParticipantToProjectForm(forms.ModelForm):
    uworker = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={'placeholder': _("email"), 'class': 'form-control'})
    )
    role = forms.CharField(
        label=_("Role"),
        widget=forms.TextInput(attrs={'placeholder': _("role"), 'class': 'form-control'})
    )
    permissions = forms.ChoiceField(
        label=_('End date'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=WORKERS_PERMISSIONS
    )

    def clean_uworker(self):

        email = self.cleaned_data["uworker"]
        try:
            ub = UserBee.objects.get(email=email)
            try:
                AssignedWorkerToProject.objects.get(uworker=ub, project=self.instance.project)
                raise forms.ValidationError(_("This user already works in this project."))
            except AssignedWorkerToProject.DoesNotExist as e:
                print e.message
                return ub
        except UserBee.DoesNotExist:
            raise forms.ValidationError(_("This user doesn't exist."))

    class Meta:
        model = Project
        fields = ['uworker', 'role', 'permissions']