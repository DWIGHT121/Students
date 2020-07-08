from django.shortcuts import render


def index(request):
    return render(request, "basics.html")


def info(request):
    return render(request, "info.html")
