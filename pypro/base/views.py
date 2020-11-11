from django.shortcuts import render


# Create your views here.
# from pypro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {})
