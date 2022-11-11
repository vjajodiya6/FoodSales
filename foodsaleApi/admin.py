from django.contrib import admin
from .models import FoodSale
from import_export.admin import ImportExportModelAdmin

@admin.register(FoodSale)
class FoodSaleAdmin(ImportExportModelAdmin):
    list_display = ('order_date','region','city','category','product','quantity','unit_price')
