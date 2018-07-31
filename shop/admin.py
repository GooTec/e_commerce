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

    def __str__(self):
        return 'Product: ' + self.name

admin.site.register(Product, ProductAdmin)


