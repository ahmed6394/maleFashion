from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('dashboard', dashboard, name='dashboard'),
    path('addProduct', addProduct, name='addProduct'),
    path('update-product/<int:pk>/', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', DeleteProduct.as_view(), name='delete-product'),
]