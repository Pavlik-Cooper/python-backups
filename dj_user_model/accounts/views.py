from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import UserCreationForm


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'register.html', {'form':form})