# Modelo de Dados do Projeto

## Categoria

- **nome**: campo de texto com até 122 caracteres.
- **descricao**: campo de texto para descrição da categoria.

### Representação de Texto

O objeto Categoria será representado pelo campo "nome".

## Post

- **titulo**: campo de texto com até 122 caracteres.
- **conteudo**: campo de texto com até 999 caracteres.
- **data**: campo de data e hora, com valor automático na criação.
- **autor**: chave estrangeira para Categoria.
- **imagem**: campo para fazer o upload de imagens, opcional.
- **resumo**: campo de texto com até 255 caracteres, opcional.
- **tags**: relação de muitos para muitos com a entidade Tag.

### Representação de Texto

O objeto Post será representado pelo campo "titulo".

## Tag

- **nome**: campo de texto com até 50 caracteres.

### Representação de Texto

O objeto Tag será representado pelo campo "nome".

## Comentarios

- **post**: chave estrangeira para Post.
- **autor**: chave estrangeira para o modelo User.
- **texto**: campo de texto para o conteúdo do comentário.
- **data**: campo de data e hora, com valor automático na criação.

---

Este é o modelo de dados do projeto, descrevendo as entidades Categoria, Post, Tag e Comentarios, juntamente com seus campos e relacionamentos. Use esta descrição como referência ao trabalhar com essas entidades em seu projeto Django.


# Rotas (URLs) do Projeto

## Categorias

- **GET /categorias/**: Retorna uma lista de categorias.
- **POST /categorias/**: Cria uma nova categoria.
- **GET /categorias/{pk}/**: Retorna detalhes de uma categoria específica.
- **PUT /categorias/{pk}/**: Atualiza uma categoria específica.
- **DELETE /categorias/{pk}/**: Exclui uma categoria específica.

## Posts

- **GET /posts/**: Retorna uma lista de posts.
- **POST /posts/**: Cria um novo post.
- **GET /posts/{pk}/**: Retorna detalhes de um post específico.
- **PUT /posts/{pk}/**: Atualiza um post específico.
- **DELETE /posts/{pk}/**: Exclui um post específico.

## Tags

- **GET /tags/**: Retorna uma lista de tags.
- **POST /tags/**: Cria uma nova tag.
- **GET /tags/{pk}/**: Retorna detalhes de uma tag específica.
- **PUT /tags/{pk}/**: Atualiza uma tag específica.
- **DELETE /tags/{pk}/**: Exclui uma tag específica.

## Comentários

- **GET /comentarios/**: Retorna uma lista de comentários.
- **POST /comentarios/**: Cria um novo comentário.
- **GET /comentarios/{pk}/**: Retorna detalhes de um comentário específico.
- **PUT /comentarios/{pk}/**: Atualiza um comentário específico.
- **DELETE /comentarios/{pk}/**: Exclui um comentário específico.

---

Essas são as rotas disponíveis em seu projeto, permitindo operações CRUD (Create, Read, Update, Delete) em categorias, posts, tags e comentários. Use esta descrição como referência ao trabalhar com as URLs em seu projeto Django.
