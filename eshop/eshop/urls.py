from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login, name="login"),
    path('registrace', views.registrace, name="registrace"),
    path('', views.index, name="index"),
    path('logout', views.logout, name="logout"),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)