from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Products
from . models import Cars
from . forms import ProductsForms
from . forms import CarsForms


# Create your views here.
def wakaru(request):
    res = {
        "name":"francis dequito"
    }
    return render(request, "index.html", res)


def about(request):
    res  ={
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


def search(request):
    print(request.get["title"])
    print(request.POST)
    return render(request, "search.html", {})


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