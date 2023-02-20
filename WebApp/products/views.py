from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from . models import Products
from . models import Cars
from . forms import ProductsForms
from . forms import CarsForms
from . forms import CircleForm
import math
import requests


# Create your views here.
# home view
def wakaru(request):
    res = {
        "name":"francis dequito"
    }
    return render(request, "index.html", res)


def about(request):
    res  = {
        "about":"This Django Web App is created by Francis Dequito as part of his Portfolio.",
        "goal":"WORK AT NASA",
        "objective":"FIND ALIENS",
        "mission":"FIND habitable exoplanets like earth. sorry i do this at work. :)"
    }
    return render(request, "about.html", res)


def hello(request):
    print(request.user)
    return HttpResponse("hi francis dequito")


def send(request):
    york = eval("2+8")
    username = "francis"
    if username!="francis":
        flag=False
    else:
        flag=True
    x=[i for i in range(20)]
    def square(n):
        return n*n
    sqx = list(map(square, x))
    return HttpResponse(f"onegai shi musi {york}\n{flag}\n{x}\n{sqx}")


def pizza(request):
    res = {
        "name":"francis dequito",
        "contact":1234,
        "pets":["sleepy","noyki","memengcat","chaw"],
        "other_name":"skaborkski"
    }
    return render(request, "pizza.html", res)


def view_product_details(request, prod_id):
    try:
        item = Products.objects.get(id=prod_id)
        res = {
        "name":item.name,
        "price":item.price,
        "desc":item.desc,
        "avail":item.avail,
        "summary":item.summary
        }
    except Products.DoesNotExist:
        raise Http404
    return render(request, "product/item_details.html", res)


def view_car_details(request, car_id):
    try:
        item = Cars.objects.get(id=car_id)
        res = {
        "brand":item.brand,
        "drive":item.drive,
        "fuel":item.fuel,
        "mileage":item.mileage,
        "owner":item.owner,
        "active":item.active
        }
    except Cars.DoesNotExist:
        raise Http404
    return render(request, "car_details.html", res)


def add_product(request):
    form = ProductsForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductsForms()
    res = {
        "form":form
    }
    return render(request, "product/item_add.html", res)


def add_cars(request):
    form = CarsForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = CarsForms()
    res = {
        "form":form
    }
    return render(request, "add_cars.html", res)


def delete_product(request, prod_id):
    obj = get_object_or_404(Products, id=prod_id)
    if request.method == "POST":
        obj.delete()
        return redirect(msg)
    res = {
        "obj":obj
    }
    return render(request, "delete_product.html", res)

def delete_car(request, car_id):
    obj = get_object_or_404(Cars, id=car_id)
    if request.method == "POST":
        obj.delete()
        return redirect(msg)
    res = {
        "obj":obj
    }
    return render(request, "delete_cars.html", res)

def msg(request):
    res = {
        "msg":"item have been deleted!"
    }
    return render(request, "product/message.html", res)


def display_products(request):
    item = Products.objects.all()
    res= {
        "items":item
    }
    return render(request, "product_list.html", res)

def display_cars(request):
    item = Cars.objects.all()
    res = {
        "items":item
    }
    return render(request, "car_list.html", res)


def get_values(request):
    print(request.GET)
    res = {
        'x': request.GET
    }
    return render(request, "input_values.html", res)


def circle_area(request):
    form = CircleForm(request.POST or None)
    circle_value = ""
    area= 0
    if form.is_valid():
        circle_value = form.cleaned_data.get("radius")
        area = math.pi*int(circle_value)*int(circle_value)
    res = {
        "form":form,
        "circle_value":circle_value,
        "area": float(area)
    }
    return render(request, "circle.html", res)


# my django web api calls. rock and roll to the world.
def web_api(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    res = {
        "response":response.json()
    }
    return render(request, "web_api.html", res)


def weather_api(request):
    data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=14.23&longitude=120.97&hourly=temperature_2m,apparent_temperature,rain,showers,weathercode,visibility,windspeed_10m,soil_temperature_0cm")
    res = {
        "data":data.json()
    }
    return render(request, "weather_api.html", res)

def air_quality_api(request):
    data = requests.get("https://air-quality-api.open-meteo.com/v1/air-quality?latitude=14.23&longitude=120.97&hourly=carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,aerosol_optical_depth,dust,ammonia&domains=cams_global&timezone=Asia%2FSingapore")
    res = {
        "data":data.json()
    }
    return render(request, "air_quality.html", res)