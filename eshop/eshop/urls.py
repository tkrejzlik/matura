from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrace', views.registrace, name="registrace"),
    path('', views.index, name="index"),

]
