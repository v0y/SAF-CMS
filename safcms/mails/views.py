from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from safcms.pages.models import Page
from .forms import ContactForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact_form_sent')
    template_name = 'mails/contact_form.html'

    def get_context_data(self, **kwargs):
        kwargs['object'] = Page.get_index()
        return super(ContactFormView, self).get_context_data(**kwargs)


class ContactFormSentView(TemplateView):
    template_name = 'mails/contact_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['object'] = Page.get_index()
        return super(ContactFormSentView, self).get_context_data(**kwargs)

