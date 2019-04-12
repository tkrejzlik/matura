from django.db import models
import json
json_dec = json.JSONDecoder()

class User(models.Model):
    username = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=300, default="")
    email = models.EmailField(default="")
    is_admin = models.BooleanField(default=False)

    def right_user(self, username, password):
        if username == self.username and self.password == password:
            return True
        return False

    def is_registred(self, username):
        if username == self.username:
            return True
        return False

    def __str__(self):
        return str(self.username)


class veci(models.Model):
    name = models.CharField(max_length=30, default="")
    cena = models.CharField(max_length=10, default="")
    obrazek = models.ImageField(blank=True,null=True)
    popis = models.CharField(max_length=200, default="")
    typ = models.CharField(max_length=15,default="")

    def __str__(self):
        return str(self.name)


