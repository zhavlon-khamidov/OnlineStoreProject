from django.urls import path
from products import views
from django.template.backends.django import DjangoTemplates

urlpatterns = [
    path('', views.productsHandler,name='products'),
    path('product/<int:pk>', views.productHandler, name='product'),
]
