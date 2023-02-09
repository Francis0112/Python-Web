from django.shortcuts import render
from django.http import HttpResponse
from . models import Products
from . models import Cars
from . forms import ProductsForms
from . forms import CarsForms


# Create your views here.
def wakaru(request):
    return render(request=request, template_name="index.html")


def about(request):
    return render(request, "about.html")


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


def view_product_details(request):
    item = Products.objects.get(id=2)
    res = {
        "name":item.name,
        "price":item.price,
        "desc":item.desc,
        "avail":item.avail,
        "summary":item.summary
    }
    return render(request, "product/item_details.html", res)


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