from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):

    #return HttpResponse("<h1>Welcome to django</h1>")
    x = Product.objects.all()
    return render(request,'index.html',{'x':x})
def about(request):
    return HttpResponse("<h1>About Page</h1>")
def contact(request):
    return HttpResponse("<h1>Contact Us</h1>")
# Create your views here.
