from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='newsdetail' )
]
