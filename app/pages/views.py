from django.views.generic.base import TemplateView

from .models import Page


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        index = Page.objects.get(is_active=True, is_index=True)
        return {'page': index}
