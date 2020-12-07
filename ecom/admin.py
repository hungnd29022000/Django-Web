# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Type, Product,Cart,Voucher,User

class TypeModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', )

class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    list_display = ('name', 'price', 'quantity', 'description','cpu','display','weight','ram','ssd')
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('product_id','count')

class VoucherModelAdmin(admin.ModelAdmin):
    list_display = ('voucher','voucherValue')



admin.site.register(Type, TypeModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Cart,CartModelAdmin)
admin.site.register(Voucher,VoucherModelAdmin)
admin.site.register(User)