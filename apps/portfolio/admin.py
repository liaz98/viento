from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'brand_title', 'year', 'brand_image', 'brand_description',)
    prepopulated_fields = {"slug" :("name",)}

@admin.register(ImageCollection)
class ImageCollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(PhotoImages)
class PhotoImagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Webdesign)
class WebdesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'web_title', 'name', 'slug', 'web_image',  'year',  'web_description',)
    prepopulated_fields = {"slug" :("name",)}

@admin.register(Colors)
class ColorsAdmin(admin.ModelAdmin):
    list_display = ('hash',)

@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'photo_title', 'year', 'photo_image', 'photo_description',)
    prepopulated_fields = {"slug" :("name",)}
