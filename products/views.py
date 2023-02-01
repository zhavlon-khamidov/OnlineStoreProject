from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def productsHandler(request):
    return render(request,'products.html')


def productHandler(request, pk):
    return HttpResponse(f"product with id {pk}")