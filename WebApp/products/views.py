from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def wakaru(request):
    return render(request=request, template_name="index.html")

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

