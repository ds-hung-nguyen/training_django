from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CreateUserForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        error_messages={
            'required': _('required_error').format(_('user_user_name')),
            'max_length': _('max_length_error').format(_('user_user_name'), 150)
        },
    )
    email = forms.EmailField(
        max_length=254,
        error_messages={
            'required': _('required_error').format(_('user_email')),
            'max_length': _('max_length_error').format(_('user_email'), 254),
            'invalid': _('email_format_error').format(_('user_email'))
        },
    )
    first_name = forms.CharField(
        max_length=150,
        error_messages={
            'required': _('required_error').format(_('user_first_name')),
            'max_length': _('max_length_error').format(_('user_first_name'), 150)
        },
    )
    last_name = forms.CharField(
        max_length=150,
        error_messages={
            'required': _('required_error').format(_('user_last_name')),
            'max_length': _('max_length_error').format(_('user_last_name'), 150)
        },
    )
    password = forms.CharField(
        max_length=128,
        error_messages={
            'required': _('required_error').format(_('user_password')),
            'max_length': _('max_length_error').format(_('user_password'), 128)
        },
    )
    password_confirm = forms.CharField(
        max_length=128,
        error_messages={
            'required': _('required_error').format(_('user_password_confirm')),
            'max_length': _('max_length_error').format(_('user_password_confirm'), 128)
        },
    )
    is_admin = forms.BooleanField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(
                _('exist_error').format(_('user_user_name'))
            )
        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError(
                _('password_not_match_error'),
                code='password_mismatch',
            )
        return password_confirm
