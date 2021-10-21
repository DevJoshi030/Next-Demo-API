from django.contrib import admin
from .models import Campaign, Subscriber


class CampaignAdmin(admin.ModelAdmin):

    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'slug')
    list_per_page = 25


class SubscriberAdmin(admin.ModelAdmin):

    list_display = ('email', 'campaign', 'created_at', 'updated_at')
    search_fields = ('email', 'campaign__title', 'created_at')
    list_per_page = 25


# Register your models here.
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
