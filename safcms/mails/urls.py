from django.conf.urls import patterns, url

from .views import (
    ContactFormSentView, ContactFormView, OrderFormSentView, OrderFormView)


urlpatterns = patterns('',
    url(r'^formularz-kontaktowy$',
        ContactFormView.as_view(), name='contact_form'),
    url(r'^formularz-kontaktowy/wyslany$',
        ContactFormSentView.as_view(), name='contact_form_sent'),
    url(r'^formularz-zamowienia$', OrderFormView.as_view(), name='order_form'),
    url(r'^formularz-zamowienia/wyslany$',
        OrderFormSentView.as_view(), name='order_form_sent'),
)
