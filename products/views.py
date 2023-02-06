from django.shortcuts import render
from django.http import HttpResponse


def productsHandler(request):
    pageName = 'All Products'; 
    authPerson = {'name':'Alisher'}
    return render(request,'products/products.html',{'page':pageName, 'auth': authPerson})


def productHandler(request, pk):
    # return HttpResponse(f"product with id {pk}")
    authPerson = None
    return render(request, 'products/single-product.html', {'page': 'Single Product','auth': authPerson})