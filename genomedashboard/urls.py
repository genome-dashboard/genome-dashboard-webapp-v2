# -*- coding: utf-8 -*-
"""genomedashboard URL Configuration"""
from __future__ import absolute_import, print_function, unicode_literals

# from cms.sitemaps import CMSSitemap
# from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve

from . import views

admin.autodiscover()

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', views.IndexView.as_view(), name='index'),
    path('polls/', include('polls.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
# ]
# This is only needed when using runserver. Do not use this in production.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [
#     url(r'^sitemap\.xml$', sitemap,
#         {'sitemaps': {'cmspages': CMSSitemap}}),
# ]

# urlpatterns += i18n_patterns(
#     re_path(r'^admin/', admin.site.urls),  # NOQA
#     re_path(r'^', include('cms.urls')),
# )

# This is only needed when using runserver.
# if settings.DEBUG:
#     urlpatterns = [
#         re_path(r'^media/(?P<path>.*)$', serve,
#             {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#         ] + staticfiles_urlpatterns() + urlpatterns
