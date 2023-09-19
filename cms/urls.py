from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', views.CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-retrieve-update-destroy'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('tags/', views.TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', views.TagRetrieveUpdateDestroyView.as_view(), name='tag-retrieve-update-destroy'),
    path('comentarios/', views.ComentariosListCreateView.as_view(), name='comentarios-list-create'),
    path('comentarios/<int:pk>/', views.ComentariosRetrieveUpdateDestroyView.as_view(), name='comentarios-retrieve-update-destroy'),
]
