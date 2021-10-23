from django.shortcuts import render,redirect
from . forms import  UserRegistrationForm

# Create your views here.
def register(request):
    context={}
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form
    else:
        form = UserRegistrationForm()
        context['register_form']=form
    return render(request,'accounts/register.html',context)
def login(request):
    return render(request, 'accounts/login.html')