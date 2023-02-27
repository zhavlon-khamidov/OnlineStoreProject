from django.shortcuts import render
from django.http import HttpResponse

data = [
    {'id':1, 'title':'Apple','price':2.3, 'description':'Apple is from Kyrgyzstan'},
    {'id':2, 'title':'Banana', 'price': 2.0, 'description':'Test Descripion'},
    {'id':3, 'title':'Lemon', 'price': 3.0, 'description':'Test Descripion'},
    {'id':4, 'title':'Watermelon', 'price': 2.0, 'description':'Test Descripion'},    
    {'id':5, 'title':'Strawberry', 'price': 5.0, 'description':'Test Descripion'},    
]

def productsHandler(request):
    pageName = 'All Products'; 
    authPerson = {'name':'Alisher'}
    return render(request,'products/products.html',
                  {'page':pageName, 'auth': authPerson,'products':data})


def productHandler(request, pk):
    # return HttpResponse(f"product with id {pk}")
    product = None
    for d in data:
        if d['id'] == pk:
            product = d
            break
            
    authPerson = None
    return render(request, 'products/single-product.html', 
                  {'page': 'Single Product','auth': authPerson,
                   'product': product})