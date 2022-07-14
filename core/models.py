from django.db import models

# Create your models here.
class User(models.Model):
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    correo = models.CharField(max_length=150)
    password = models.CharField(max_length=150)