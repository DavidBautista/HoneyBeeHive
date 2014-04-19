from django import forms
from bee.models import UserBee
from auth_validation import send_activation_mail
from django.utils.translation import ugettext_lazy as _
import datetime


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
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
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="E-Mail")

    class Meta:
        model = UserBee
        fields = ("email", "first_name", "last_name")

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            UserBee.objects.get(email=email)
        except UserBee.DoesNotExist:
            return email
        raise forms.ValidationError("A user with that email address already exists.")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email_active = False
        user.is_active = False
        user.date_joined=datetime.datetime.now()
        send_activation_mail(user)
        user.save()