from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from products.models import Product
from .forms import ProductForm

# data = [
#     {'id':1, 'title':'Apple','price':2.3, 'description':'Apple is from Kyrgyzstan'},
#     {'id':2, 'title':'Banana', 'price': 2.0, 'description':'Test Descripion'},
#     {'id':3, 'title':'Lemon', 'price': 3.0, 'description':'Test Descripion'},
#     {'id':4, 'title':'Watermelon', 'price': 2.0, 'description':'Test Descripion'},    
#     {'id':5, 'title':'Strawberry', 'price': 5.0, 'description':'Test Descripion'},    
# ]

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('products')
    return render(request, 'products/delete.html',{'product':product})

def createProduct(request : HttpRequest):
    form = ProductForm()
    print(request.method)
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {"form": form}
    return render(request,'products/product-form.html',context)

def editProduct(request : HttpRequest, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    print(request.method)
    
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product',product.id)
    context = {"form": form}
    return render(request,'products/product-form.html',context)

def category(request, category):
    products = Product.objects.filter(category__name=category)
    return render(request, 'products/products.html',{'products':products})

def productsHandler(request):
    pageName = 'All Products'; 
    products = Product.objects.all()
    authPerson = {'name':'Alisher'}
    return render(request,'products/products.html',
                  {'products':products})


def productHandler(request, pk):
    # return HttpResponse(f"product with id {pk}")
    product = Product.objects.get(id=pk)
    # for d in data:
    #     if d['id'] == pk:
    #         product = d
    #         break
            
    authPerson = None
    return render(request, 'products/single-product.html', 
                  {'page': 'Single Product','auth': authPerson,
                   'product': product})