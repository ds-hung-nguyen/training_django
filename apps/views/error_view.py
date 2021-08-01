from django.shortcuts import render


def not_found_handler(request, exception):
    return render(request, 'errors/404.html', {})


def internal_error_handler(request, exception=None):
    return render(request, 'errors/500.html', {})


def permission_denied_handler(request, exception=None):
    return render(request, 'errors/403.html', {})


def bad_request_handler(request, exception=None):
    return render(request, 'errors/400.html', {})
