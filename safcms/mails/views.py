from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact_form_sent')
    template_name = 'mails/contact_form.html'


class ContactFormSentView(TemplateView):
    template_name = 'mails/contact_form_sent.html'
