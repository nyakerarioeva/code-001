from django.shortcuts import render, HttpResponse,redirect
from . models import Catalogue, CustomerEntry

# Create your views here.
def post(request):
    result = Catalogue.objects.all()
    ctx = {"res":result}
    return render(request,'main/dashboard.html', ctx)
def Entry(request,pk):
    
    return render(request, "entry.html")
        
def product(request):
    return render(request, 'main/product.html')