from django.contrib import admin

from .models import Message
from users_messages.models import Image


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 0


class MessageAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]
    search_fields = ['from_user', 'to_user']
    list_display = ['title', 'from_user', 'to_user']
    list_filter = ['is_read']
    class Meta:
        model = Message

admin.site.register(Message, MessageAdmin)
