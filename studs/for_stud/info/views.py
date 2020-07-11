from django.shortcuts import render, redirect
from .forms import InfoForm
from .models import Info
from django.http import HttpResponse


def index(request):
    return render(request, "basics.html")


def info(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')

    data = {'form': form}

    return render(request, "info.html", data)


def login(request):
    if request.method == "POST":
        username = request.POST('username')
        password = request.POST('password')
        username_data = Info.objects.get(
            username='username', password='password').first()
        if username_data:
            name = username_data.name
            return redirect('/index', name='name')

    return render(request, "login.html")
