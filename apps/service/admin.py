from django.contrib import admin
from .models import *


@admin.register(Service)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'service_description', 'service_image',)
    prepopulated_fields = {"slug" :("name",)}


@admin.register(ServiceList)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description',)