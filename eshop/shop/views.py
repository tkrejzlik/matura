from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from shop.models import User


def index(request):
    return render(request, "index.html", {"users": User.objects.all()})


def login(request):
    return render(request, "login.html")

def registrace(request):
    if request.method == "GET":
        return render(request, "registrace.html")
    elif request.method == "POST":
        password = request.POST.get("pass1", "")
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        if username and password:
            if not User.objects.filter(username=username):
                user = User(username=username, password=password,email=email)
                user.save()
                request.session["username"] = username
                return redirect("/")
        return render(request, "registrace.html",{"error": "Tento uživatel již existuje!"})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        password = request.POST.get("pass1", "")
        username = request.POST.get("username", "")
        if User.objects.filter(username=username, password=password):
            request.session["username"] = username
            return redirect("/")
        return render(request, "login.html", {"error2": "Bad username or password!"})



