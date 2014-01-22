from django.conf.urls import patterns, url

from .views import IndexView, PageView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w\d-]+)$', PageView.as_view(), name='page'),
)
