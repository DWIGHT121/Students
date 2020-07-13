from django.shortcuts import render, redirect
from .forms import InfoForm
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        username_data = Info.objects.get(
            username='username').first()
        if username_data:
            if password == Info.objects.get(username="username").first().password:
                name = username_data.name
                return redirect('/', name='name')

    return render(request, "login.html")
