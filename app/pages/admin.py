from django.contrib import admin

from .models import Image, MenuItem, Page


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(Image, ImageAdmin)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'parent', 'article')
admin.site.register(MenuItem, MenuItemAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = \
        ('name', 'menu_item')
    fieldsets = (
        (None, {
            'fields':
                ('name', 'content', 'menu_item', 'images')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
admin.site.register(Page, PageAdmin)
