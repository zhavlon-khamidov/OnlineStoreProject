from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('products')


def login_user(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        # next = request.POST['next'] if request.POST.__contains__("next") else ''
        print(next)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("products")
        else:
            print("Username or Password is incorrect")
            
    context = {
        'next': request.GET['next']
    }
        
    return render(request,'login.html')