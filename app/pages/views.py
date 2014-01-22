from django.views.generic import DetailView

from .models import Page


class IndexView(DetailView):
    template_name = 'pages/index.html'

    def get_object(self, queryset=None):
        return Page.get_index()


class PageView(DetailView):
    model = Page
