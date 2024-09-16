from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.
class Base(View):
    views = {}

class Home(Base):
    def get(self,request):
        self.views['products'] = Product.objects.all()
        return render(request,'index.html',self.views)
class Shop(Base):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['shops'] = Product.objects.all()
        self.views['filters'] = Filter_price.objects.all()
        Cat_id = request.GET.get("categories")
        Filter_price_id = request.GET.get("filters")
        print(Cat_id)
        if Cat_id :
            self.views['shops'] = Product.objects.filter(category=Cat_id)
        elif Filter_price_id:
            self.views['shops'] = Product.objects.filter(filter_price=Filter_price_id)
        else:
            self.views['shops'] = Product.objects.all()

        return render(request, 'product.html',self.views)
