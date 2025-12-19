from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('actor', 'verb', 'recipient', 'timestamp', 'read')
    list_filter = ('read', 'timestamp')
    search_fields = ('actor__username', 'recipient__username', 'verb')

