from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login, name="login"),
    path('registrace', views.registrace, name="registrace"),
    path('', views.index, name="index"),
    path('logout', views.logout, name="logout"),
]
