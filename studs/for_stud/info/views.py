from django.shortcuts import render, redirect
from .forms import InfoForm


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
