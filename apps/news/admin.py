from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_post_title', 'slug')
    prepopulated_fields = {"slug" :("news_post_title",)}