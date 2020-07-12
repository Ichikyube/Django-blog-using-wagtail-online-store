from django.shortcuts import render

def page_not_found(request, exception=None, template_name='404.html'):
    return render(request, "errors/404.html", {})

def server_error(request, exception=None, template_name='500.html'):
    return render(request, "errors/500.html", {})

def permission_denied(request, exception=None, template_name='404.html'):
    return render(request, "errors/404.html", {})

def bad_request(request, exception=None, template_name='404.html'):
    return render(request, "errors/404.html", {})
