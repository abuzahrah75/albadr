from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class Kategori(MPTTModel):
    nama = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['nama']
    
    def __str__(self):
        return self.nama


class Projek(models.Model):
    nama = models.CharField(max_length=200)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Struktur(MPTTModel):
    nama = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # jenis = 
    data = models.JSONField(null=True)

    class MPTTMeta:
        order_insertion_by = ['nama']
    
    def __str__(self):
        return self.nama
