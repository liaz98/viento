from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class PortfolioAll(ListView):
    template_name = 'portfolio/all.html'
    model = Webdesign
    context_object_name = 'web'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = Brand.objects.order_by('year')[:3]
        context['photo'] = Photography.objects.order_by('year')[:3]
        return context
        
class PortfolioWeb(ListView):
    model = Webdesign
    template_name = 'portfolio/web.html'
    context_object_name = 'web'

class PortfolioWebDetail(DetailView):
    model = Webdesign
    template_name = 'portfolio/webdetail.html'
    context_object_name = 'web'


class PortfolioBrand(ListView):
    model = Brand
    template_name = 'portfolio/brand.html'
    context_object_name = 'brand'

class PortfolioPhoto(ListView):
    model = Photography
    template_name = 'portfolio/photo.html'
    context_object_name = 'photo'



class PortfolioBrandDetail(DetailView):
    model = Brand
    template_name = 'portfolio/branddetail.html'
    context_object_name = 'brand'
    # queryset = Brand.objects.all()[:4]



class PortfolioPhotoDetail(DetailView):
    model = Photography
    template_name = 'portfolio/photodetail.html'
    context_object_name = 'photo'