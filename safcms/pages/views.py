from django.views.generic import DetailView

from .models import Page


class PageView(DetailView):
    model = Page

    def get_object(self, queryset=None):
        if not self.kwargs['slug']:
            return Page.get_index()
        else:
            return super(PageView, self).get_object(queryset)
