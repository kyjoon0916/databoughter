from django.http import request
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def model(request):
    return render(request, 'model.html')


def model2(request):
    return render(request, 'model2.html')


def label(request):
    return render(request, 'label.html')


def test(request):
    return render(request, 'test.html')


def company(request):
    return redirect('https:/smartinside.ai')
