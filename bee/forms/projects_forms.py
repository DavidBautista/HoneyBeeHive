from django import forms
from bee.models import Project, UserStory
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
