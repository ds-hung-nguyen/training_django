from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.shortcuts import redirect


@require_GET
@login_required
def index(request):
    if request.user.is_superuser:
        return redirect(reverse('users.index'))
    return redirect(reverse('posts.index'))
