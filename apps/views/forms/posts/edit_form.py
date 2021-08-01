from django import forms
from django.utils.translation import gettext as _


class EditPostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        error_messages={
            'required': _('required_error').format(_('post_title')),
            'max_length': _('max_length_error').format(_('post_title'), 200)
        },
    )
    body = forms.CharField(
        error_messages={
            'required': _('required_error').format(_('post_body'))
        },
    )
