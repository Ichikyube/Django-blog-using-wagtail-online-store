from django.conf import settings
from django.conf.urls import include, url, handler400, handler403, handler404, handler500, re_path
from django.views.static import serve
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.static import static
from search import views as search_views
from blog import views as blog_views
handler400 = 'blog.views.bad_request'
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^404/$', blog_views.page_not_found),

    re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, }),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SERVE_MEDIA_FILES:
    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
