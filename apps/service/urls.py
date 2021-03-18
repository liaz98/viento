from django.urls import path
from .views import *

urlpatterns = [
    path('', Services.as_view(), name='service'),
    path('service/<str:slug>/', ServicesDetail.as_view(), name='servicedetail' )
]
