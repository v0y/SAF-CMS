from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # third party
    url(r'^themes/', include('themes.urls')),

    # internal
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('safcms.pages.urls')),
)


if settings.DEBUG:
    urlpatterns += \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
