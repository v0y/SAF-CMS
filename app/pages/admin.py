from django.contrib import admin

from .models import Image, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name')
    fieldsets = (
        (None, {
            'fields':
                ('name', 'is_active', 'is_in_menu', 'is_index', 'content',
                 'images')
        }),
        ('Advanceds', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
admin.site.register(Page, PageAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(Image, ImageAdmin)
