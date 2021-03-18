from django.urls import path
from .views import *

urlpatterns = [
    path('', PortfolioAll.as_view(), name='port_all'),
    path('web/', PortfolioWeb.as_view(), name='web'),
    path('brand/', PortfolioBrand.as_view(), name='brand'),
    path('photo/', PortfolioPhoto.as_view(), name='photo'),
    path('web/<str:slug>/', PortfolioWebDetail.as_view(), name='webdetail'),
    path('brand/<str:slug>/', PortfolioBrandDetail.as_view(), name='branddetail'),
    path('photo/<str:slug>/', PortfolioPhotoDetail.as_view(), name='photodetail'),
]
