from ninja import NinjaAPI, Redoc
from blog.models import Post, Category, Hashtag
from django.contrib.auth.models import User
from .models import PostInputSchema, PostOutputSchema, HashtagOutputSchema, MessageSchema

api = NinjaAPI(docs=Redoc())


@api.get("dummy")
def get_dummy(request):
    results = { "hello": "world" }
    return results


@api.get("post")
def get_posts(request):
    posts = Post.objects.all().order_by("fecha")
    results = []
    for post in posts:
        result = {
            "id": post.id,
            "titulo": post.titulo,
            "fecha": post.fecha,
            "autor": post.autor.username,
            "categoria": post.categoria.id,
            "hashtags": [],
        }
        for etiqueta in post.etiquetas.all():
            result["hashtags"].append(etiqueta.nombre)
        results.append(result)
    return results


@api.get("post/{id}", response={200:PostOutputSchema, 404:MessageSchema})
def get_post(request, id):
    post = Post.objects.filter(id=id)
    if post is None or len(post) == 0:
        return 404, { 'message': 'Post not found' }
    post = post[0]
    results = {
        "id": post.id,
        "titulo": post.titulo,
        "texto": post.texto,
        "fecha": post.fecha.strftime("%d/%m/%Y"),
        "autor": post.autor.username,
        "categoria": post.categoria.nombre,
        # "hashtags": [],
    }
    # for etiqueta in post.etiquetas.all():
        # results["hashtags"].append({"nombre": etiqueta.nombre})
    print(results)
    return results
    
    
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