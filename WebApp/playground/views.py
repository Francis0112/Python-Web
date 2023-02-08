from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("hallo world i am under the water please help me.")

def hackerman(request):
    return HttpResponse("i am the hackerman! whaha")

def login(request):
    return render(request, 'index.html', {'name':'francis'}) 

def add(request):
    n = [i for i in range(1,10+1)]
    return HttpResponse(n)

