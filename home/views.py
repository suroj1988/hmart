from django.shortcuts import render,redirect
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

class Search(Base):
    def get(self,request):
        if request.method == "GET":
            query = request.GET.get("query")
            if query == "":
                return redirect("/")
            else:
                self.views['searchproducts'] = Product.objects.filter(name__icontains=query)

        return render(request,'search.html',self.views)
class ProductDetail(Base):
    def get(self,request,slug):
        self.views
        self.views['detail_products'] = Product.objects.filter(slug=slug)
        return render(request,'product-detail.html',self.views)

def Contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        date = request.POST.get("date")

        contact = Contact_us.objects.create(
            name = name,
            email = email,
            message = message,
            subject = subject,
            date = date,
        )
        contact.save()
        return redirect("/")
    return render(request,'contact.html')