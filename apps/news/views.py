from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News 


class NewsList(ListView):
    model = News
    template_name = 'news/blog.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = News
    template_name = 'news/blog_detail.html'
    context_object_name = 'news'
     

