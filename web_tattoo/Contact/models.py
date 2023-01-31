from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    query_text = models.CharField(max_length=360)

    def __str__(self):
        return f'Nombre: {self.name}, Email: {self.email}, Consulta: {self.query_text}'