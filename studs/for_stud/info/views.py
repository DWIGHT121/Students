from django.shortcuts import render, redirect
from .forms import InfoForm, LoginForm
from .models import Info
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "basics.html")


def info(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = {'form': form}

    return render(request, "info.html", data)


def login(request):
    if request.method == "POST":
        user_info = LoginForm(request.POST)
        return render(request, "after_info.html", {"username": user_info})
    else:
        return render(request, "login.html", {})
