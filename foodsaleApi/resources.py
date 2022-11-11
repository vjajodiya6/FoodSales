from import_export import resources
from .models import FoodSale

class FoodSaleResource(resources.ModelResource):
    class meta:
        model = FoodSale