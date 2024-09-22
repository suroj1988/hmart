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
        self.views['brands'] = Brand.objects.all()
        Brand_id = request.GET.get("brand")
        Cat_id = request.GET.get("categories")
        Filter_price_id = request.GET.get("filters")
        AtoZ_slug = request.GET.get("AtoZ")
        ZtoA_slug = request.GET.get("ZtoA")
        LtoH_id = request.GET.get("LtoH")
        HtoL_id = request.GET.get("HtoL")
        New_id = request.GET.get("New_product")
        Hot_id = request.GET.get("Hot_product")
        print(Cat_id)
        if Cat_id :
            self.views['shops'] = Product.objects.filter(category=Cat_id)
        if Brand_id :
            self.views['shops'] = Product.objects.filter(brand=Brand_id)
        elif Filter_price_id:
            self.views['shops'] = Product.objects.filter(filter_price=Filter_price_id)
        elif AtoZ_slug:
            self.views['shops'] = Product.objects.filter().order_by('name')
        elif ZtoA_slug:
            self.views['shops'] = Product.objects.filter().order_by('-name')
        elif LtoH_id:
            self.views['shops'] = Product.objects.filter().order_by('price')
        elif HtoL_id:
            self.views['shops'] = Product.objects.filter().order_by('-price')
        elif New_id:
            self.views['shops'] = Product.objects.filter(label='new')
        elif Hot_id:
            self.views['shops'] = Product.objects.filter(label='hot')
        else:
            self.views['shops'] = Product.objects.all()

        return render(request, 'product.html',self.views)
