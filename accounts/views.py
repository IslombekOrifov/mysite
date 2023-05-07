from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import CustomUser
from .forms import LoginForm, RegisterForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                                request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:index')
                else:
                    messages.error('Disabled account')
            else:
                messages.error("Invalid login")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
            user_form.cleaned_data['password'])
            new_user.save()
            messages.success("Your account has been succesfully created. Now you can log-in.")
            return render(request, 
                          'registration/login.html')
    else:
        user_form = RegisterForm()
    return render(request, 'registration/login.html', {'user_form': user_form})

def user_logout(request):
    logout(request)
    return redirect('main:index')
