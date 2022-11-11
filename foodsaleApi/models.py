from django.db import models

class FoodSale(models.Model):
    order_date = models.DateField()
    region = models.CharField(max_length=4)
    city = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    product = models.CharField(max_length=25)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2,max_digits=5)

    def __str__(self):
        return self.product

