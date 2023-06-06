from django.contrib import admin
from .models import products
# Register your models here.

class productsAdmin(admin.ModelAdmin):
    list_display=('prodname', 'prod_price', 'prod_stock')


admin.site.register(products, productsAdmin)