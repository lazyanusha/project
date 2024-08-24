# anime/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'apps/index.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                auth_login(request, user)
                print("User authenticated and logged in:", user)
                return redirect('index')
            else:
                print("User not authenticated")
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Invalid email or password")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'apps/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login') 
        else:
            messages.error(request, "Error occurred during signup")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'apps/signup.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('index')  # Ensure 'index' is a valid URL pattern name
