from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contacts/', Contact.as_view(), name='contacts'),
    path('about/', About.as_view(), name='about'),

]
