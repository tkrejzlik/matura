from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
from shop.models import User,veci


def index(request):
    username = request.session.get("username")
    return render(request, "index.html", {"users": User.objects.all(),"veci": veci.objects.all(),"user":username})


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
        return render(request, "login.html", {"error2": "Špatné jméno nebo heslo!"})

def logout(request):
    del request.session["username"]
    return redirect("/")

def kola(request):
    username = request.session.get("username")
    return render(request, "kola.html", {"users": User.objects.all(), "veci": veci.objects.all(), "user": username})

def lyze(request):
    username = request.session.get("username")
    return render(request, "lyze.html", {"users": User.objects.all(), "veci": veci.objects.all(), "user": username})

def brusle(request):
    username = request.session.get("username")
    return render(request, "brusle.html", {"users": User.objects.all(), "veci": veci.objects.all(), "user": username})

def buy(request):
    if request.method == "GET":
        id = request.GET.get("id", None)
        username = request.session.get("username")
        vec= veci.objects.get(id=id)
        return render(request, "buy.html", {"users": User.objects.all(), "user": username,"item":vec})
