from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from apps.support.helper import constants
from django.utils.translation import gettext as _
from .forms.auth.login_form import LoginForm
from login_required import login_not_required
from django.views.decorators.http import require_POST


@login_not_required
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == constants('HTTP_METHOD_POST') and form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('top.index'))
        else:
            messages.error(request, _('invalid_login'))
    return render(request, 'auth/login.html', {'title': _('Login'), 'form': form})


@require_POST
def logout(request):
    auth_logout(request)
    return redirect(reverse('auth.login'))
