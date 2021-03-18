from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from  ..portfolio.models import *
from .models import *
from ..service.models import Service
from .forms import ContactFormForm


def get_contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactFormForm()
    return render(request,
                  'home/contacts.html',
                  {
                      'form': form,
                  })


class Index(View):
    template_name = 'home/index.html'
    model = Slider

    def get(self, request):
        slider = Slider.objects.all().first()
        service = Service.objects.all()[:6]
        brand = Brand.objects.order_by('year')[:3]
        web = Webdesign.objects.order_by('year')[:3]
        photo = Photography.objects.order_by('year')[:3]
        context = {
            'brand' : brand,
            'web' : web,
            'photo': photo,
            'slider' : slider,
            'service' : service,
        }
        return render(request, self.template_name, context)


class Contact(View):
    template_name = 'home/contacts.html'
    model = Contacts

    def get(self, request):
        contacts = Contacts.objects.all().first()
        context = {
            'contacts': contacts,
        }
        return render(request, self.template_name, context)


class About(TemplateView):
    template_name = 'home/about.html'


