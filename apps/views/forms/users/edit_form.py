from django import forms
from django.utils.translation import gettext as _


class EditUserForm(forms.Form):
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
    is_admin = forms.BooleanField(required=False)
