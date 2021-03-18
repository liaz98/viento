from django.db import models
from django.urls import reverse

class ImageGallery(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Picture name')
    gallery = models.ImageField(upload_to='brand/gallery', blank=True, verbose_name='Brand gallery')

    def __str__(self):
        return self.title

class ImageCollection(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Picture name')
    image = models.ImageField(upload_to='brand/image_col', blank=True, verbose_name='Image collection')

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(max_length=120, blank=True, verbose_name='Brand name')
    slug = models.SlugField(max_length=120, unique=True)
    brand_title = models.CharField(max_length=200, blank=True, verbose_name='Brand title')
    year = models.DateField(null=True, blank=True, verbose_name='Brand year')
    brand_image = models.ImageField(upload_to='brand/images', blank=True, verbose_name='Brand image')
    brand_image_cover = models.ImageField(upload_to='brand/images', blank=True, verbose_name='Brand Cover')
    brand_description = models.TextField(blank=True)
    image_col = models.ManyToManyField(ImageCollection, blank=True, verbose_name='Brand Image collection' )
    gallery = models.ManyToManyField(ImageGallery, blank=True, verbose_name='brand image gallery')
    client = models.CharField(max_length=150, blank=True, verbose_name='Client Name')
    service = models.CharField(max_length=150, blank=True, verbose_name='Service Name')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    
    def get_absolute_url(self):
        return reverse('branddetail', kwargs={'slug':self.slug})


#-----------------| WEB PORTFOLIO |----------------->


class Colors(models.Model):
    hash = models.CharField(max_length=10, blank=True, verbose_name='Ranglar')

    def __str__(self):
        return self.hash

class Webdesign(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Web type')
    slug = models.SlugField(max_length=200, unique=True)
    web_title = models.CharField(max_length=200, blank=True, verbose_name='Web title')
    year = models.DateField(null=True, blank=True, verbose_name='web year')
    web_image = models.ImageField(upload_to='web/images', blank=True, verbose_name='Web Image front')
    web_image_pc = models.ImageField(upload_to='web/images', blank=True, verbose_name='Detail Image PC')
    web_image_mobile = models.ImageField(upload_to='web/images', blank=True, verbose_name='Detail Image MOBILE')
    client = models.CharField(max_length=150, blank=True, verbose_name='Client Name')
    service = models.CharField(max_length=150, blank=True, verbose_name='Service Name')
    web_description = models.TextField(blank=True, verbose_name='About project')
    web_image_full = models.ImageField(upload_to='web/images', blank=True, verbose_name='Web_Full_Image')
    colors_pattern = models.ManyToManyField(Colors, blank=True, verbose_name='Colors')
    typography1 = models.CharField(max_length=50, blank=True, verbose_name='Typography Primary')
    typography2 = models.CharField(max_length=50, blank=True, verbose_name='Typography Primary')



    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'web'
        verbose_name_plural = 'webs'
    
    def get_absolute_url(self):
        return reverse('webdetail', kwargs={'slug': self.slug})

#<-----------------| PHOTOGRAPHY |----------------->

class PhotoImages(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Photo Portfolio')
    pictures  = models.ImageField(upload_to='portfolio/photo', blank=True, verbose_name='Photography Portfolio')

    def __str__(self):
        return self.title

class Photography(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='photography name')
    slug = models.SlugField(max_length=200, blank=True, verbose_name='photography slug')
    year = models.DateField(null=True, blank=True, verbose_name='photo year')
    photo_image = models.ImageField(upload_to='photo/images', blank=True, verbose_name='photography image')
    photo_description = models.TextField(blank=True)
    photo_title = models.CharField(max_length=200, blank=True, verbose_name='photo title')
    client = models.CharField(max_length=50, blank=True, verbose_name='Client')
    service = models.CharField(max_length=50, blank=True, verbose_name='Service')
    pictures = models.ManyToManyField(PhotoImages, blank=True, verbose_name='Portfolio Photo')


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together =(('id', 'slug'),)
        verbose_name = 'photography'
        verbose_name_plural = 'photographies'
        
    def get_absolute_url(self):
        return reverse('photodetail', kwargs={'slug': self.slug})