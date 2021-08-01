from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from apps.support.helper import constants
from django.utils.translation import gettext as _
from apps.services.post_service import PostService
from .forms.posts.edit_form import EditPostForm
from .forms.posts.create_form import CreatePostForm
from apps.decorators.auth import admin_required
from login_required import login_not_required


@require_GET
def index(request):
    return render(request, 'posts/index.html', {'title': _('post_list_page_title')})


@require_GET
def show(request, post_id):
    try:
        post = PostService().get_by_id(post_id)
    except ObjectDoesNotExist:
        raise Http404(_('record_not_exist'))
    return render(request, 'posts/show.html', {'title': _('post_show_page_title'), 'post': post})


def create(request):
    form = CreatePostForm(request.POST or None, user=request.user)
    if request.method == constants('HTTP_METHOD_POST') and form.is_valid():
        PostService().create(form.cleaned_data)
        messages.success(request, _('create_record_success'))
        return redirect(reverse('posts.index'))
    return render(request, 'posts/create.html', {'title': _('post_create_page_title'), 'form': form})


def edit(request, post_id):
    try:
        form = EditPostForm(request.POST or None)
        if request.method == constants('HTTP_METHOD_POST') and form.is_valid():
            PostService().update(post_id, form.cleaned_data)
            messages.success(request, _('update_record_success'))
            return redirect(reverse('posts.index'))
        return render(request, 'posts/edit.html', {'title': _('post_edit_page_title'), 'post': PostService().get_by_id(post_id), 'form': form})
    except ObjectDoesNotExist:
        raise Http404(_('record_not_exist'))


@require_POST
def delete(request, post_id):
    try:
        PostService().delete(post_id)
        return JsonResponse({'message': _('delete_record_success')})
    except ObjectDoesNotExist:
        return JsonResponse({'message': _('record_not_exist')}, status=404)


@require_POST
def search(request):
    params = request.POST.dict()
    if not request.user.is_superuser:
        params['author'] = request.user.id
    return JsonResponse(PostService().search(params))


@require_POST
@login_not_required
def list(request):
    return JsonResponse(PostService().approved_list(request.POST), safe=False)


@require_POST
@admin_required
def approved(request, post_id):
    try:
        PostService().approved(post_id)
        return JsonResponse({'message': _('approved_record_success')})
    except ObjectDoesNotExist:
        return JsonResponse({'message': _('record_not_exist')}, status=404)
