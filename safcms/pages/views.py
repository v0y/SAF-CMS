from django.http import Http404
from django.views.generic import DetailView

from .models import Page


class PageView(DetailView):
    model = Page
    context_object_name = 'page'

    def get_object(self, queryset=None):
        if not self.kwargs['slug']:
            return Page.get_index()
        else:
            obj = super(PageView, self).get_object(queryset)
            parents = reversed(self.kwargs.get('parents', '').split('/'))

            menu_item = obj.menu_item
            if menu_item:
                for parent_slug in parents:
                    menu_item = menu_item.parent
                    if (
                            menu_item and
                            menu_item.parent and
                            parent_slug != menu_item.get_slug()
                    ):
                        raise Http404()

            return obj
