from django.contrib import admin
from .models import VirtualPrivateServer


class VirtualPrivateServerAdmin(admin.ModelAdmin):
    """Admin class for model VirtualPrivateServer."""

    list_display = ('pk', 'uid', 'cpu', 'ram', 'hdd',)
    search_fields = ('uid', 'cpu', 'ram', 'hdd',)
    list_filter = ('cpu', 'ram', 'hdd',)
    empty_value_display = '-пусто-'


admin.site.register(VirtualPrivateServer, VirtualPrivateServerAdmin)
