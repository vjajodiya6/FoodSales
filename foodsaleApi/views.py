from django.shortcuts import render
from .models import FoodSale
from .serializers import FoodSalesSerializer
from django.contrib import messages
from .resources import FoodSaleResource
from tablib import Dataset
from rest_framework import filters,generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter


def upload(request):
    if request.method == 'POST':
        food_resource = FoodSaleResource()
        dataset = Dataset()
        new_food = request.FILES['myfile']

        if not new_food.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'excel.html')

        imported_data = dataset.load(new_food.read(),format='xlsx')
        for data in imported_data:
            value = FoodSale(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
            )
            value.save()
    return render(request,'excel.html')


class ProductName(generics.ListCreateAPIView):
    search_fields = ['product']
    filter_backends = (filters.SearchFilter,)
    queryset = FoodSale.objects.all()
    serializer_class = FoodSalesSerializer

class ProductNamePost(ListAPIView):
    queryset = FoodSale.objects.all()
    serializer_class = FoodSalesSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['product']
