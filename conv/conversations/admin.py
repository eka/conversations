from django.contrib import admin
from conversations.models import Conversation

admin.site.register(Conversation, admin.ModelAdmin)