from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
from shop.models import User, veci, Items


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
                request.session["email"] = email
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
    del request.session["email"]
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
        request.session["vec"] = vec.id
        return render(request, "buy.html", {"users": User.objects.all(), "user": username,"item":vec})

def basket(request):
    vysledna_cena = 0
    username = request.session.get("username")
    if request.method == "GET":
        action = request.GET.get("action", None)
        id = request.GET.get("id", None)
        if action == 'delete':
            Items.objects.filter(user=User.objects.get(username=username), id=id).delete()

    if request.method == "POST":
        vec = request.session["vec"]
        Items(user=User.objects.get(username=username),item=veci.objects.get(id=vec)).save()

    user_items = Items.objects.filter(user=User.objects.get(username=username))
    for user_item in user_items:
        vysledna_cena += user_item.item.cena

    return render(request, "basket.html", {"items": Items.objects.filter(user=User.objects.get(username=username)),"user": username, "vysledna_cena": vysledna_cena})

def send(request):
    string = ""
    vysledna_cena = 0
    username = request.session.get("username")
    email = request.session.get("email")
    user_items = Items.objects.filter(user=User.objects.get(username=username))
    string+= "Děkujeme za nákup v krejzlík eshop!!" + "\n" + "objednané produkty: " + "\n"
    for user_item in user_items:
        string += user_item.item.name + " "
        string += str(user_item.item.cena)+" kč" + "\n"
        vysledna_cena+=user_item.item.cena
    string+= "\n"
    string+= "vysledna cena: " + str(vysledna_cena) + " kč"

    print(email)
    print(string)
    send_mail('objednavka',string,'eshop.krejzlik@gmail.com',[email],fail_silently=False)

    return redirect("/")
