from django.conf import settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from fiut.helpers import simple_send_email

from safcms.pages.models import Page
from .forms import ContactForm, PrintOrderForm, ProjectOrderForm


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
            'From': '"Formularz kontaktowy" <%s>' %
                settings.DEFAULT_FROM_EMAIL,
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


class PrintOrderFormView(FormView):
    form_class = PrintOrderForm
    success_url = reverse_lazy('print_order_form_sent')
    template_name = 'mails/print_order_form.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(PrintOrderFormView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        site_name = Site.objects.get_current().name
        data = form.data

        subject = \
            "[%s] Formularz zamówienia wydruku" % site_name
        headers = {
            'From': '"Formularz zamówienia wydruku" <%s>' %
                settings.DEFAULT_FROM_EMAIL,
            'Reply-To': '"%s" <%s>' % (data.get('name', ''), data['email']),
        }

        simple_send_email(
            subject=subject,
            message='mails/print_order_form_mail_content.txt',
            recipients=settings.EMAIL_RECIPIENT,
            headers=headers,
            attachments=dict(form.files),
            message_data=data,
        )

        return super(PrintOrderFormView, self).form_valid(form)


class PrintOrderFormSentView(TemplateView):
    template_name = 'mails/print_order_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(PrintOrderFormSentView, self).get_context_data(**kwargs)


class ProjectFormView(FormView):
    form_class = ProjectOrderForm
    success_url = reverse_lazy('project_order_form_sent')
    template_name = 'mails/project_order_form.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(ProjectFormView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        site_name = Site.objects.get_current().name
        data = form.data

        subject = \
            "[%s] Formularz zamówienia projektu" % site_name
        headers = {
            'From': '"Formularz zamówienia projektu" <%s>' %
                    settings.DEFAULT_FROM_EMAIL,
            'Reply-To': '"%s" <%s>' % (data.get('name', ''), data['email']),
        }

        simple_send_email(
            subject=subject,
            message='mails/project_order_form_mail_content.txt',
            recipients=settings.EMAIL_RECIPIENT,
            headers=headers,
            attachments=dict(form.files),
            message_data=data,
        )

        return super(ProjectFormView, self).form_valid(form)


class ProjectFormSentView(TemplateView):
    template_name = 'mails/project_order_form_sent.html'

    def get_context_data(self, **kwargs):
        kwargs['page'] = Page.get_index()
        return super(ProjectFormSentView, self).get_context_data(**kwargs)

