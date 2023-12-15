from ninja import NinjaAPI, Redoc
from blog.models import Post, Category, Hashtag
from django.contrib.auth.models import User
from .models import PostInputSchema, PostOutputSchema, HashtagOutputSchema, MessageSchema
from typing import List

# Creamos un objeto para manipular la API
api = NinjaAPI(docs=Redoc())


# Servicio dummy solo para comprobar que la API funciona
@api.get("dummy", response={200:MessageSchema})
def get_dummy(request):
    results = { 'message': 'hello world' }
    return results


@api.get("post", response={200:List[PostOutputSchema]})
def get_posts(request):
    posts = Post.objects.all().order_by("fecha")
    results = []
    for post in posts:
        result = {
            "id": post.id,
            "titulo": post.titulo,
            "texto": post.texto,
            "fecha":  post.fecha.strftime("%d/%m/%Y"),
            "autor": {
                "id": post.autor.id,
                "username": post.autor.username,
            },
            "categoria": {
                "id": post.categoria.id,
                "nombre": post.categoria.nombre,
            },
            "hashtags": [],
        }
        for etiqueta in post.etiquetas.all():
            hashtag = {
                "id": etiqueta.id, 
                "nombre": etiqueta.nombre,
            }
            result["hashtags"].append(hashtag)
        results.append(result)
    return results


@api.get("post/{id}", response={200:PostOutputSchema, 404:MessageSchema})
def get_post(request, id):
    post = Post.objects.filter(id=id)
    if post is None or len(post) == 0:
        return 404, { 'message': 'Post not found' }
    post = post[0]
    result = {
        "id": post.id,
        "titulo": post.titulo,
        "texto": post.texto,
        "fecha":  post.fecha.strftime("%d/%m/%Y"),
        "autor": {
            "id": post.autor.id,
            "username": post.autor.username,
        },
        "categoria": {
            "id": post.categoria.id,
            "nombre": post.categoria.nombre,
        },
        "hashtags": [],
    }
    for etiqueta in post.etiquetas.all():
        hashtag = {
            "id": etiqueta.id, 
            "nombre": etiqueta.nombre,
        }
        result["hashtags"].append(hashtag)
    return result
    
    
@api.post("post", response={200:MessageSchema, 404:MessageSchema})
def save_post(request, p: PostInputSchema):
    author = User.objects.filter(id=p.autor)
    if author is None or len(author) == 0:
        return 404, { 'message': 'Author not found' }
    category = Category.objects.filter(id=p.categoria)
    if category is None or len(category) == 0:
        return 404, { 'message': 'Category not found' }
    post = {
        "titulo": p.titulo,
        "texto": p.texto,
        "autor": author[0],
        "categoria": category[0],
    }
    post = Post.objects.create(**post)
    return { 'message': 'Post has been created' }


@api.delete("post/{id}", response={200:MessageSchema, 404:MessageSchema})
def delete_post(request, id: int):
    post = Post.objects.filter(id=id)
    if post is None or len(post) == 0:
        return 404, { 'message': 'Post not found' }
    post.delete()
    return { 'message': 'Post has been deleted' }