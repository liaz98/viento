from django.contrib import admin
from .models import *



@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'address', )

@admin.register(ContactFormUs)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'message', )