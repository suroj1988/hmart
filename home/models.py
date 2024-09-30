from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    def __str__(self):
         return self.name

class Filter_price(models.Model):
    Filter = (('0 to 10000','0 to 10000'),
              ('10000 to 20000','10000 to 20000'),
              ('20000 to 30000','20000 to 30000'),
              ('30000 to 40000','30000 to 40000'))
    price = models.CharField(choices=Filter,max_length=200)
    slug = models.CharField(max_length=300, unique=True)


    def __str__(self):
        return self.price
class Colour(models.Model):
     name = models.CharField(max_length=200)
     code = models.CharField(max_length=200,unique=True)
     slug = models.CharField(max_length=300, unique=True)

     def __str__(self):
         return self.name
class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name
LABELS = (('new','New'),('hot','Hot'),('','default'))
STOCK = (('INSTOCK','INSTOCK'),('OUTSTOCK','OUTSTOCK'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300,unique=True)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_price, on_delete=models.CASCADE)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    label = models.CharField(choices=LABELS,max_length=200)
    stock = models.CharField(choices=STOCK, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
class Images(models.Model):
    image = models.ImageField(upload_to='media')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class Tags(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.email
