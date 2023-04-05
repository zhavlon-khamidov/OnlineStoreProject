from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('products')


def register_user(request):
    userForm = CustomUserCreationForm()
    if request.method == "POST":
        userForm = CustomUserCreationForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('products')
    context = {"form": userForm}
    return render(request, "register.html", context)

def login_user(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET['next'] if request.POST.__contains__("next") else ''
        next = next if len(next)>0 else 'products'
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)
        else:
            print("Username or Password is incorrect")
        
    return render(request,'login.html')