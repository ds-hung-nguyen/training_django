from django import forms
from django.utils.translation import gettext as _


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        error_messages={
            'required': _('required_error').format(_('user_user_name')),
            'max_length': _('max_length_error').format(_('user_user_name'), 150)
        },
    )
    password = forms.CharField(
        max_length=128,
        error_messages={
            'required': _('required_error').format(_('user_password')),
            'max_length': _('max_length_error').format(_('user_password'), 128)
        },
    )
