from django.shortcuts import render, HttpResponse

# Create your views here.
def post(request):
    return render(request,'main/dashboard.html')
def product(request):
    return render(request, 'main/product.html')