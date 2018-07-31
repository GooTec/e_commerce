from django.contrib import admin

# Register your models here.
from .cores.models import Profile, Product, ProductImgs, Cart, CartItem

class ProductImgsInline(admin.StackedInline):
    model = ProductImgs
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product information',
         {'fields': ['category','price']}),
        ('Product detail', {'fields': ['content','main_img','recommend']}),
    ]
    inlines =  [ProductImgsInline]

admin.site.register(Product, ProductAdmin)


