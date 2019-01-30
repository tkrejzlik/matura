from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def registrace(request):
    return render(request, "registrace.html")
