from django.urls import path
from products import views
from django.template.backends.django import DjangoTemplates

urlpatterns = [
    path('', views.productsHandler,name='products'),
    path('product/<str:pk>', views.productHandler, name='product'),
    path('category/<str:category>',views.category, name="category"),
    path('create',views.createProduct, name="createProduct"),
    path('edit/<str:pk>', views.editProduct, name="editProduct"),
    path('delete/<str:pk>', views.deleteProduct, name="deleteProduct"),

]
