from rest_framework import serializers
from . import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Categoria
        fields=('__all__')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Post
        fields=('__all__')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentarios
        fields = '__all__'