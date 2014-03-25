from django.conf.urls import patterns, url

from ..views import (
    ContactFormSentView, ContactFormView, OrderFormSentView, OrderFormView)


urlpatterns = patterns('',
    url(r'^kontaktowy$',
        ContactFormView.as_view(), name='contact_form'),
    url(r'^kontaktowy/wyslany$',
        ContactFormSentView.as_view(), name='contact_form_sent'),
    url(r'^zamowienia$', OrderFormView.as_view(), name='order_form'),
    url(r'^zamowienia/wyslany$',
        OrderFormSentView.as_view(), name='order_form_sent'),
    url(r'^zamowienia/wyslany$',
        OrderFormSentView.as_view(), name='order_form_sent'),
)
