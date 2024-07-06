from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    SignupForm,
    LoginForm,
    EmailChangeForm,
)

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

@login_required
def user_logout(request):
    logout(request)
    return redirect('recipes:index')

@login_required
def user_account(request):
    return render(request, "user_account/account_page.html")

@login_required
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed.')
            return redirect('user:account')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "user_account/change_password.html", {'form':form})

@login_required
def user_email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your email has been changed.')
            return redirect('user:account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmailChangeForm(user=request.user, initial={'email': request.user.email})
    return render(request, "user_account/change_email.html", {'form': form})
