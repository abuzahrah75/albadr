from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Kategori, Projek, Struktur
# Register your models here.

class CustomMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Kategori, CustomMPTTModelAdmin)
admin.site.register(Projek)
admin.site.register(Struktur, CustomMPTTModelAdmin)