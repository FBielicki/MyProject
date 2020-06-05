"""Forms for users app."""

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.password_validation import password_validators_help_texts
from django.utils.translation import gettext_lazy as _

from users.models import User


class RegistrationForm(UserCreationForm):

    """Registration form."""

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text='<br></br>'.join(password_validators_help_texts()),
    )

    # add placeholder and hover text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "placeholder": field.label,
                    "data-container": "body",
                    "data-toggle": "popover",
                    "data-trigger": "hover",
                    "data-placement": "right", "data-content": field.help_text,
                    "id": field.label
                }
            )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class LoginForm(AuthenticationForm):

    """Login form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': _('Username'),
             'class': 'test'}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': _('Password')}
        )


class TeacherForm(forms.ModelForm):

    #courses = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all())
    #is_subscribing = BoolChar()

    """Teacher form."""

    class Meta:
        model = User
        fields = ('courses', 'is_subscribing')


class ChangeForm(UserChangeForm):

    # add placeholder and hover text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "placeholder": field.label,
                    "data-container": "body",
                    "data-toggle": "popover",
                    "data-trigger": "hover",
                    "data-placement": "right", "data-content": field.help_text,
                    "id": field.label
                }
            )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangePasswordForm(PasswordChangeForm):

    """Change Password form."""

    # add placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'placeholder': _('Old Password')}
        )
        self.fields['new_password1'].widget.attrs.update(
            {'placeholder': _('New Password')}
        )
        self.fields['new_password2'].widget.attrs.update(
            {'placeholder': _('Confirm New Password')}
        )
