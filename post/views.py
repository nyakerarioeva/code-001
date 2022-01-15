from django.shortcuts import render, HttpResponse,redirect
from . models import Catalogue, CustomerEntry

# Create your views here.
def post(request):
    result = Catalogue.objects.all()
    ctx = {"res":result}
    return render(request,'main/dashboard.html', ctx)
def Entry(request,pk):
    result = Catalogue.objects.get(id=pk)
    ctx = {"res":result}
    return render(request, "entry.html", ctx)
        
def product(request):
    return render(request, 'main/product.html')