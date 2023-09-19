from rest_framework import generics
from .models import Categoria, Post, Tag, Comentarios
from .serializers import CategoriaSerializer, PostSerializer, TagSerializer, ComentariosSerializer
from django_filters import rest_framework as filters
#from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    ordering_fields = ['nome', 'descricao']
    filterset_fields=['nome']
    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    ordering_fields = ['nome', 'descricao']
    authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ['titulo', 'autor']
    authentication_classes = [JWTAuthentication]
   # permission_classes = [IsAuthenticated]

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    ordering_fields = ['titulo', 'autor']
    authentication_classes = [JWTAuthentication]
   # permission_classes = [IsAuthenticated]

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ComentariosListCreateView(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

class ComentariosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer