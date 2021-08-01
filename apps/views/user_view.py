from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from apps.support.helper import constants
from django.utils.translation import gettext as _
from apps.services.user_service import UserService
from .forms.users.edit_form import EditUserForm
from .forms.users.create_form import CreateUserForm
from apps.decorators.auth import admin_required


@require_GET
@admin_required
def index(request):
    return render(request, 'users/index.html', {'title': _('user_list_page_title')})


@require_GET
@admin_required
def show(request, user_id):
    try:
        user = UserService().get_by_id(user_id)
    except ObjectDoesNotExist:
        raise Http404(_('record_not_exist'))
    return render(request, 'users/show.html', {'title': _('user_show_page_title'), 'user': user})


@admin_required
def create(request):
    form = CreateUserForm(request.POST or None)
    if request.method == constants('HTTP_METHOD_POST') and form.is_valid():
        UserService().create(form.cleaned_data)
        messages.success(request, _('create_record_success'))
        return redirect(reverse('users.index'))
    return render(request, 'users/create.html', {'title': _('user_create_page_title'), 'form': form})


@admin_required
def edit(request, user_id):
    try:
        form = EditUserForm(request.POST or None)
        if request.method == constants('HTTP_METHOD_POST') and form.is_valid():
            UserService().update(user_id, form.cleaned_data)
            messages.success(request, _('update_record_success'))
            return redirect(reverse('users.index'))
        return render(request, 'users/edit.html', {'title': _('user_edit_page_title'), 'user': UserService().get_by_id(user_id), 'form': form})
    except ObjectDoesNotExist:
        raise Http404(_('record_not_exist'))


@require_POST
@admin_required
def delete(request, user_id):
    try:
        UserService().delete(user_id)
        return JsonResponse({'message': _('delete_record_success')})
    except ObjectDoesNotExist:
        return JsonResponse({'message': _('record_not_exist')}, status=404)


@require_POST
@admin_required
def search(request):
    data = UserService().search(request.POST)
    return JsonResponse(data)
