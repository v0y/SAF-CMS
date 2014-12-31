from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # third party
    url(r'^themes/', include('themes.urls')),

    # internal
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('safcms.pages.urls')),
)

# urls for 3d.askra.pl
if settings.SITE_ID == 2:
    favico_url = '%s3d.askra.pl/shared/imgs/favicon.ico' % settings.STATIC_URL

    urlpatterns += patterns('',
        url(r'^formularz/', include('safcms.mails.urls.d_askra_pl')),
        (r'^favicon\.ico$', RedirectView.as_view(url=favico_url)),
    )

# redirect to right page even if user used appending slash
urlpatterns += patterns('',
    ('^(?P<x>.+)/$', RedirectView.as_view(url='/%(x)s', permanent=True)))

if settings.DEBUG:
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
