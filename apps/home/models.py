from django.db import models


class Slider(models.Model):
    heading1 = models.CharField(max_length=200, blank=True, verbose_name='Slider Heading 1')
    heading2 = models.CharField(max_length=200, blank=True, verbose_name='Slider Heading 2')
    desc = models.CharField(max_length=200, blank=True, verbose_name='Opisanie')
    photo = models.ImageField(upload_to='slider/images', blank=True, verbose_name='Slider photo')
    photo_map = models.ImageField(upload_to='slider/images', blank=True, verbose_name='Slider photo map')
    video = models.CharField(max_length=200, blank=True, verbose_name='Slider Background Video')

    def __str__(self):
        return self.heading1

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


class Contacts(models.Model):
    phone = models.CharField(max_length=18, blank=True, verbose_name='Phone Company')
    email = models.EmailField(blank=True, verbose_name='Email Company')
    address = models.CharField(max_length=200, blank=True, verbose_name='Company address')
    logo = models.ImageField(upload_to='contact/images', blank=True, verbose_name='Company logo')
    image = models.ImageField(upload_to='contact/images', blank=True, verbose_name='Company image')

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class ContactFormUs(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='name')
    phone = models.CharField(max_length=16, blank=True, verbose_name='phone')
    subject = models.CharField(max_length=60, blank=True, verbose_name='subject')
    message = models.TextField(blank=True, verbose_name='message')

    def __str__(self):
        return self.name
