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

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
# from carts.views import cart_home
from store.accounts.views import LoginView, RegisterView, guest_register_view
from store.addresses.views import checkout_address_create_view
from store.billing.views import payment_method_view
from store.carts.views import cart_detail_api_view
from store.views import home_page, about_page, contact_page

# from products.views import (
#                                 ProductListView, 
#                                 product_list_view, 
#                                 ProductDetailView, 
#                                 ProductDetailSlugView, 
#                                 product_detail_view,
#                                 ProductFeaturedListView,
#                                 ProductFeaturedDetailView
#                             )

handler400 = 'blog.views.bad_request'
handler403 = 'blog.views.permission_denied'
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^store/$', home_page, name='home'),
    url(r'^about/$', about_page,name='about'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/cart/',cart_detail_api_view, name='api-cart'),
    url(r'^cart/', include("carts.urls", namespace='cart')),
    url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^products/', include("products.urls", namespace='products')),
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
