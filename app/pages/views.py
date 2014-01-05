from django.views.generic.base import TemplateView
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        return {'media': settings.MEDIA_ROOT}
