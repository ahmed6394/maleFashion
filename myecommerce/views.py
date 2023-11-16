from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .forms import *

from .models import *

# Create your views here.
def home(request):
    products = Products.objects.all()
    context = { 'products': products}
    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        
    context = {'form':form}
    return render (request, 'contact.html', context)

def addProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form':form}
    return render (request, 'products.html', context)

def dashboard(request):
    products = Products.objects.all()
    context = { 'products': products}
    return render(request, 'dashboard.html', context)


class UpdateProduct(UpdateView):
    model = Products
    fields = "__all__"
    template_name = 'products_form.html'
    success_url = reverse_lazy('dashboard')
    
    
class DeleteProduct(DeleteView):
    model = Products
    context_object_name = 'product'
    template_name = 'delete.html'
    success_url = reverse_lazy('dashboard')