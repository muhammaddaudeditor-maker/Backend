# home/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import HomeHero, HomeStat, HomeIntro, HomeSkill, HomeService, HomeProcess, HomeTool, HomeFAQ, HomeCTA

@admin.register(HomeHero)
class HomeHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_preview', 'is_active', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    list_editable = ['is_active']

    fieldsets = (
        ('Hero Information', {
            'fields': ('title', 'typewriter_phrases', 'subtitle', 'video', 'primary_button_text', 'secondary_button_text')
        }),
        ('Display Settings', {
            'fields': ('is_active',)
        }),
    )

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="100" height="60" controls>'
                '<source src="{}" type="video/mp4"></video>',
                obj.video.url
            )
        return "No video"
    video_preview.short_description = 'Video Preview'

@admin.register(HomeStat)
class HomeStatAdmin(admin.ModelAdmin):
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

@admin.register(HomeIntro)
class HomeIntroAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'is_active', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['title', 'subtitle']
    list_editable = ['is_active']

    fieldsets = (
        ('Intro Information', {
            'fields': ('title', 'subtitle', 'image', 'achievements', 'primary_button_text', 'secondary_button_text')
        }),
        ('Display Settings', {
            'fields': ('is_active',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="60" style="object-fit: cover;" />',
                obj.image.url
            )
        return "No image"
    image_preview.short_description = 'Image Preview'

@admin.register(HomeSkill)
class HomeSkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Skill Information', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HomeService)
class HomeServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Service Information', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HomeProcess)
class HomeProcessAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Process Information', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HomeTool)
class HomeToolAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active', 'icon']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Tool Information', {
            'fields': ('title', 'description', 'icon')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HomeFAQ)
class HomeFAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['question', 'answer']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('FAQ Information', {
            'fields': ('question', 'answer')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )

@admin.register(HomeCTA)
class HomeCTAAdmin(admin.ModelAdmin):
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