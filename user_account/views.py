from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = SignupForm()
    return render(request, "user_account/signup.html", {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('recipes:index')
    else:
        form = LoginForm()
    return render(request, 'user_account/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('recipes:index')