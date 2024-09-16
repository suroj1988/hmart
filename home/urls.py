from .views import *
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shop/', Shop.as_view(), name='shop'),
]