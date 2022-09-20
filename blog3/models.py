from django.db import models

class Flotante(models.Model):
    dato1 = models.FloatField(blank=True, null=True)
    dato2 = models.FloatField(blank=True, null=True)
    dato3 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.dato1)+' , '+str(self.dato2)+' , '+str(self.dato3)