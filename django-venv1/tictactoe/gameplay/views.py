from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "gameplay/home.html")

def test(request):
    return render(request, "gameplay/test.html")