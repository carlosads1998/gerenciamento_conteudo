from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome=models.CharField(max_length=122)
    descricao=models.TextField()

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    titulo=models.CharField(max_length=122)
    conteudo=models.TextField(max_length=999)
    data=models.DateField(auto_now_add=True)
    autor=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem=models.ImageField(upload_to='imagens/', blank=True, null=True)
    resumo= models.TextField(max_length=255, blank=True,null=True)
    tags=models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.titulo

class Tag(models.Model):
    nome=models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Comentarios(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto=models.TextField()
    data=models.DateField(auto_now_add=True)