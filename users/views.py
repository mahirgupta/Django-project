import imp
from django.shortcuts import render,redirect
from .forms import register_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'congrats {username} created')
            return redirect('login')
    else :
        form = register_form()
    return render(request,'register.html',{'form':form})

@ login_required
def profile(request):
    return render(request, 'profile.html')
