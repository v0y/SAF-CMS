from django.conf.urls import patterns, url

from .views import ContactFormSentView, ContactFormView


urlpatterns = patterns('',
    url(r'^formularz-kontaktowy$',
        ContactFormView.as_view(), name='contact_form'),
    url(r'^formularz-kontaktowy/wyslany$',
        ContactFormSentView.as_view(), name='contact_form_sent'),

)
