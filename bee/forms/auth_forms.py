from django import forms
from bee.models import UserBee
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
import datetime


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={'placeholder': _("Email"),
                                       'class': 'form-control input-md margin-centered input-login'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'placeholder': _("Password"),
                                          'class': 'form-control input-md margin-centered input-login'})
    )
    error_messages = {'not_active': _("Your account is not active, please check your email."),
                      'invalid': _("Incorrect email or password.")}

    class Meta:
        model = UserBee
        fields = ['email', 'password']

    def clean(self):
        self.cleaned_data['user'] = self._authenticate()
        return self.cleaned_data

    def _authenticate(self):
        self.non_field_errors()
        user = authenticate(username=self.cleaned_data.get('email', None),
                            password=self.cleaned_data.get('password', None))
        if not user:
            raise forms.ValidationError(self.error_messages['invalid'], code='invalid')
        elif not user.is_active:
            raise forms.ValidationError(self.error_messages['not_active'], code='not_active')
        return user


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={'placeholder': _("Password"), 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'placeholder': _("Repeat password"),
                                          'class': 'form-control'}),
        help_text=_("Enter the same password as above, for verification."))

    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
        }

    class Meta:
        model = UserBee

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'], code='password_mismatch')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit: user.save()
        return user


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="E-Mail",
        widget=forms.EmailInput(attrs={'placeholder': _("Email"),
                                       'class': 'form-control'}),
    )
    first_name = forms.CharField(
        label=_("First name"),
        widget=forms.TextInput(attrs={'placeholder': _("First name"),
                                      'class': 'form-control'})
    )
    last_name = forms.CharField(
        label=_("Last name"),
        widget=forms.TextInput(attrs={'placeholder': _("Last name"),
                                      'class': 'form-control'})
    )

    class Meta:
        model = UserBee
        fields = ("email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            UserBee.objects.get(email=email)
        except UserBee.DoesNotExist:
            return email
        raise forms.ValidationError(_("A user with that email address already exists."))

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email_active = False
        user.is_active = False
        user.date_joined = datetime.datetime.now()
        user.send_activation_mail()
        user.save()
        return user