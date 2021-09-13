from django.contrib import admin
from .models import Category
from .models import UnitMeasurement
from .models import Products
# Register your models here.

@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ['name','description' ]
    search_fields = ['name']
    list_per_page = 5

admin.site.register(UnitMeasurement)

@admin.register(Products)
class ProductsAdmin (admin.ModelAdmin):
    list_display = ['product','description','unit_price','amount']
    search_fields = ['product']
    list_editable = ['unit_price', 'amount']
    list_per_page = 10