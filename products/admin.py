from django.contrib import admin
from .models import Customer, Product, Order, OrderItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at', 'complete')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
