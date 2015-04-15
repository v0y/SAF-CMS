from django.conf.urls import patterns, url

from .views import PageView


urlpatterns = patterns('',
    url(r'^(?P<slug>[\w\d-]*)$', PageView.as_view(), name='page'),
    url(r'^(?P<parents>[\w\d\-/]*)/{1}(?P<slug>[\w\d-]*)$',
        PageView.as_view(),
        name='page'
    ),
)
