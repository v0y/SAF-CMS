from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from fiut.helpers import simple_send_email

from safcms.pages.models import Page
from .forms import ContactForm, PrintOrderForm


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact_form_sent')
    template_name = 'mails/contact_form.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(ContactFormView, self).get_context_data(**kwargs)
    
    def form_valid(self, form):
        site_name = Site.objects.get_current().name
        data = form.data
        subject = \
            "[%s] Formularz kontaktowy: %s" % (site_name, data['subject'])
        headers = {
            'From': '"Formularz kontaktowy" <%s>' % settings.DEFAULT_FROM_EMAIL,
            'Reply-To': '"%s" <%s>' % (data['name'], data['email']),
        }

        simple_send_email(
            subject=subject,
            message=data['text'],
            recipients=settings.EMAIL_RECIPIENT,
            headers=headers,
        )

        return super(ContactFormView, self).form_valid(form)


class ContactFormSentView(TemplateView):
    template_name = 'mails/contact_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(ContactFormSentView, self).get_context_data(**kwargs)


class OrderFormView(FormView):
    form_class = PrintOrderForm
    success_url = reverse_lazy('order_form_sent')
    template_name = 'mails/order_form.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(OrderFormView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        site_name = Site.objects.get_current().name
        data = form.data

        subject = \
            "[%s] Formularz zamówienia" % site_name
        headers = {
            'From': '"Formularz zamówienia" <%s>' % settings.DEFAULT_FROM_EMAIL,
            'Reply-To': '"%s" <%s>' % (data.get('name', ''), data['email']),
        }

        simple_send_email(
            subject=subject,
            message='mails/order_form_mail_content.txt',
            recipients=settings.EMAIL_RECIPIENT,
            headers=headers,
            attachments=dict(form.files),
            message_data=data,
        )

        return super(OrderFormView, self).form_valid(form)


class OrderFormSentView(TemplateView):
    template_name = 'mails/order_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(OrderFormSentView, self).get_context_data(**kwargs)


class ProjectFormSentView(TemplateView):
    template_name = 'mails/project_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(ProjectFormSentView, self).get_context_data(**kwargs)

