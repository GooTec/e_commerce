from django.contrib import admin

# Register your models here.
from .cores.models import Profile, Product, ProductImgs, Cart, CartItem, Order , OrderItem

class ProductImgsInline(admin.StackedInline):
    model = ProductImgs
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product information',
         {'fields': ['category','name','price']}),
        ('Product detail', {'fields': ['content','main_img','recommend']}),
    ]
    inlines =  [ProductImgsInline]


class ProfileAdmin(admin.ModelAdmin):
    exclude=("user_id",)
    readonly_fields=('user_id', )

    fieldsets = [
        ('User information',
        {'fields' : ['fullname', 'phone', 'address', 'address_detail']})
    ]


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    exclude = ("user_id",)
    readonly_fields = ("user_id",)

    fieldsets =[
        ("OrderInfo",
         {'fields' : ['fullname', 'phone','address','address_detail', 'total']}
         )
    ]
    inlines =  [OrderItemInline]


admin.site.register(Product, ProductAdmin)

admin.site.register(CartItem)

admin.site.register(Profile ,ProfileAdmin)

admin.site.register(Order, OrderAdmin)
