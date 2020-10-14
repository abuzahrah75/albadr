from django.db import models

class UntukBeli(models.Model):
    nama = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nama
    
