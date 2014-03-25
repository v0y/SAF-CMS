from django.conf.urls import patterns, url

from ..views import (
    ContactFormSentView, ContactFormView, OrderFormSentView, OrderFormView,
    ProjectFormSentView)


urlpatterns = patterns('',
    # contact form
    url(r'^kontakt$',
        ContactFormView.as_view(), name='contact_form'),
    url(r'^kontakt/wyslany$',
        ContactFormSentView.as_view(), name='contact_form_sent'),

    # print 3D
    url(r'^zamowenie/wydruk$', OrderFormView.as_view(), name='order_form'),
    url(r'^zamowenie/wydruk/wyslany$',
        OrderFormSentView.as_view(), name='order_form_sent'),

    # project 3D
    url(r'^zamowenie/projekt/wyslany$',
        ProjectFormSentView.as_view(), name='project_form_sent'),
)
