from django.urls import path
from products import views
from django.template.backends.django import DjangoTemplates

urlpatterns = [
    path('', views.productsHandler),
    path('product/<str:pk>', views.productHandler),
]
