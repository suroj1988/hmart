from .views import *
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shop/', Shop.as_view(), name='shop'),
    path('search', Search.as_view(), name='search'),
    path('detail_product/<slug>', ProductDetail.as_view(), name='detail_product'),
]