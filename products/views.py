from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from products.models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# data = [
#     {'id':1, 'title':'Apple','price':2.3, 'description':'Apple is from Kyrgyzstan'},
#     {'id':2, 'title':'Banana', 'price': 2.0, 'description':'Test Descripion'},
#     {'id':3, 'title':'Lemon', 'price': 3.0, 'description':'Test Descripion'},
#     {'id':4, 'title':'Watermelon', 'price': 2.0, 'description':'Test Descripion'},    
#     {'id':5, 'title':'Strawberry', 'price': 5.0, 'description':'Test Descripion'},    
# ]

@login_required(login_url='/login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('products')
    return render(request, 'products/delete.html', {'product': product})


@login_required(login_url='/login')
def createProduct(request: HttpRequest):
    form = ProductForm()
    print(request.method)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {"form": form}
    return render(request, 'products/product-form.html', context)


@login_required(login_url='/login')
def editProduct(request: HttpRequest, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    print(request.method)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', product.id)
    context = {"form": form}
    return render(request, 'products/product-form.html', context)


def category(request, category):
    products = Product.objects.filter(category__name=category)
    return render(request, 'products/products.html', {'products': products})


def productsHandler(request):
    products = Product.objects.all()
    page = 1
    if request.GET.get('page'):
        page = int(request.GET['page'])
    paginator = Paginator(products, 4)
    try:
        products = paginator.page(page)
    except:
        products = paginator.page(paginator.num_pages)

    page_range = paginator.page_range
    page_start = 1
    page_end = paginator.num_pages
    if paginator.num_pages > 10:
        page_start = products.number - 5 if products.number - 5 > 1 else 1
        page_end = products.number + 5 if products.number + 5 < paginator.num_pages else paginator.num_pages
        page_range = range(page_start, page_end + 1)

    return render(request, 'products/products.html',
                  {
                      'products': products,
                      'page_range': page_range,
                      'page_start':page_start,
                      'page_end':page_end,
                      'paginator':paginator,
                  })


def productHandler(request, pk):
    # return HttpResponse(f"product with id {pk}")
    product = Product.objects.get(id=pk)
    # for d in data:
    #     if d['id'] == pk:
    #         product = d
    #         break

    authPerson = None
    return render(request, 'products/single-product.html',
                  {'page': 'Single Product', 'auth': authPerson,
                   'product': product})
