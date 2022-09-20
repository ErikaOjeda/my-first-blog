from django.db import models

class Entero(models.Model):
    dato1 = models.IntegerField(blank=True, null=True)
    dato2 = models.IntegerField(blank=True, null=True)
    dato3 = models.IntegerField(blank=True, null=True)

