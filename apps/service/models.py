from django.db import models
from django.urls import reverse

class ServiceList(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='Service title')
    description = models.TextField(blank=True, verbose_name='Service description')
    image = models.ImageField(upload_to='service/image', blank=True, verbose_name='Service image')

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Service name')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Service slug')
    title = models.CharField(max_length=200, blank=True, verbose_name='Title in Detail')
    service_description = models.TextField(blank=True, verbose_name='Service description')
    service_image = models.ImageField(upload_to='services/images', verbose_name='Service image')
    services = models.ManyToManyField(ServiceList, blank=True, verbose_name='Choose service')


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'service'
        verbose_name_plural = 'services'
    
    def get_absolute_url(self):
        return reverse('servicedetail', kwargs={'slug': self.slug})
