from django.contrib import admin

from .models import Box, Image, MenuItem, Page


class BoxAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'codename',)
    fieldsets = (
        (None, {
            'fields': ('page', 'name', 'content')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('codename', 'content_type')
        }),
    )
admin.site.register(Box, BoxAdmin)


class BoxIneline(admin.TabularInline):
    model = Box


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
    inlines = [MenuItemInline, ImageInline, BoxIneline]
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
