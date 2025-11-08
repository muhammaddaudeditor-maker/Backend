# about/admin.py (Updated)

from django.contrib import admin
from django.utils.html import format_html
from .models import Stat, CoreValue, TimelineEvent, Skill, AboutCTA, AboutTabContent

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'suffix', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['name']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Stat Information', {
            'fields': ('name', 'value', 'suffix', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Value Information', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['year', 'title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Event Information', {
            'fields': ('year', 'title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['name']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'level', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(AboutCTA)
class AboutCTAAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active']

    fieldsets = (
        ('CTA Information', {
            'fields': ('title', 'description', 'button_text')
        }),
        ('Display Settings', {
            'fields': ('is_active',)
        }),
    )

@admin.register(AboutTabContent)
class AboutTabContentAdmin(admin.ModelAdmin):
    list_display = ['tab_name', 'title', 'is_active', 'created_at']
    list_filter = ['is_active', 'tab_name']
    search_fields = ['title', 'content']
    fields = ['tab_name', 'title', 'content', 'image', 'is_active']

    from django.contrib import admin
from .models import AboutTabContent
