from django.contrib import admin
from .models import Sale, SaleProduct, SubType, Product, Table

# Register your models here.
admin.site.register(Sale)
admin.site.register(SaleProduct)
admin.site.register(SubType)
admin.site.register(Product)
admin.site.register(Table)
