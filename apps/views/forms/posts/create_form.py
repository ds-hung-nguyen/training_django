from django import forms
from django.utils.translation import gettext as _


class CreatePostForm(forms.Form):
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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        if self.user.is_authenticated:
            data['author'] = self.user.id
        return self.cleaned_data
