from django.contrib import admin
from .models import *
class ImagesInline(admin.TabularInline):
    model = Images
class TagsInline(admin.TabularInline):
    model = Tags
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,TagsInline]
# Register your models here.
admin.site.register(Category)
admin.site.register(Colour)
admin.site.register(Filter_price)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Tags)
