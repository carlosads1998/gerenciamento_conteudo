import django_filters
from .models import Categoria, Post

class CategoriaFilter(django_filters.FilterSet):
    nome=django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Categoria
        fields = ['nome']

class PostFilter(django_filters.FilterSet):
    nome=django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Post
        fields = ['titulo']