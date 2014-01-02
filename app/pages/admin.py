from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'name')
    fieldsets = (
        (None, {
            'fields': ('name', 'is_active', 'content', 'image')
        }),
        ('Advanceds', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
    )
admin.site.register(Page, PageAdmin)
