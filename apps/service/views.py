from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Services(ListView):
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'service'

class ServicesDetail(DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'service'