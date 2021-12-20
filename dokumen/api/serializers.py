# from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from dokumen.models import Projek, Kategori

class KategoriSerializer(serializers.ModelSerializer):
    # nama = RecursiveField()
    # children = serializers.ListField(child=RecursiveField())
    class Meta:
        model = Kategori
        fields = "__all__"

class ProjekSerializer(serializers.ModelSerializer):
    # kategori = serializers.RelatedField(source='kategori', read_only=True)
    # kategori = serializers.RelatedField(read_only=True)
    kategori = KategoriSerializer(read_only=True)
    class Meta:
        model = Projek
        fields = "__all__"

