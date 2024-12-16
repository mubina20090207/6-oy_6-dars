from django.shortcuts import render, get_object_or_404
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'cars/home.html', {'brands': brands, 'cars': cars})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = brand.cars.all()
    return render(request, 'cars/brand_detail.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})
