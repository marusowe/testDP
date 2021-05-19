from django.contrib import admin
from urlshort_api.models import UrlShort


@admin.register(UrlShort)
class UrlShortAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_url', 'hash', 'short_url', 'user_session_key', 'created_at',)
    readonly_fields = ('short_url', 'user_session_key')

