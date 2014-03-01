from django.contrib import admin

from .models import Image, MenuItem, Page


class ImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(Image, ImageAdmin)


class ImageInline(admin.TabularInline):
    model = Image


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'parent', 'page')
admin.site.register(MenuItem, MenuItemAdmin)


class MenuItemInline(admin.TabularInline):
    model = MenuItem


class PageAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline, ImageInline]
    list_display = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'short', 'content')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('slug', 'content_type')
        }),
    )
admin.site.register(Page, PageAdmin)
