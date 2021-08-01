from django.http import Http404, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from login_required import login_not_required


@require_GET
@login_not_required
def index(request):
    return render(request, 'sites/index.html', {'title': _('site_list_page_title')})
