from django.contrib import admin
from .models import Categoria, Post, Tag, Comentarios

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comentarios)
