from django.db import models
from django.urls import reverse

class News(models.Model):
    news_post_image = models.ImageField(upload_to='news/images', blank=True, verbose_name='News post image')
    news_post_title = models.CharField(max_length=200, blank=True, verbose_name='News post title')
    news_post_date = models.DateTimeField(auto_now=True, verbose_name='News post date')
    description = models.TextField(blank=True, verbose_name='Description')
    slug = models.SlugField(max_length=50, verbose_name='Slug')

    def __str__(self):
        return self.news_post_title

    class Meta:
        ordering = ('news_post_title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'new'
        verbose_name_plural = 'news'

    def get_absolute_url(self):
        return reverse('newsdetail', kwargs={'slug': self.slug})