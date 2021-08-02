from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Products,Order
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description="default category"
    list_display=('title','price','discount_price','category','image','description')
    search_fields=('description',)
    action=('change_category_to_default')
    fields=('title','price')


admin.site.register(Products,ProductsAdmin)
admin.site.register(Order)
