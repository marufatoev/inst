from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from blog.models import Profile


def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('users:sign_in')
    return render(request, 'register.html', {'form': form})


def sign_in(request):
    form = SignInForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('blog:home')
    return render(request, 'login.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')


def edit_profile(request):
   form = EditProfileForm(request.POST, instance=request.user)
   if form.is_valid() and request.method == 'POST':
       user = form.save()
       update_session_auth_hash(request, user)
       return redirect('blog:home')
   form = EditProfileForm(instance=request.user)
   return render(request, 'edit_profile.html', {'form': form})
