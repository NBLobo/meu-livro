from django.db import models
from datetime import datetime


class Livro(models.Model):
    titulo = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    resenha = models.TextField(max_length=500)
