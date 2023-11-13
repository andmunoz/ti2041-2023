from django.shortcuts import render
from .models import Post, Category, Hashtag


def index(request, post_id = None, category_id = None, hashtag_id = None):
    # Obtenemos todas las categorías y las etiquetas
    categories = Category.objects.all().order_by("nombre")
    hashtags = Hashtag.objects.all().order_by("nombre")

    # Obtenemos las publicaciones filtradas por categoría, etiqueta o mostrar todas
    posts = None
    if category_id:
        posts = Post.objects.filter(categoria__id = category_id).order_by("-fecha")
    elif hashtag_id:
        posts = Post.objects.filter(etiquetas__id = hashtag_id).order_by("-fecha")
    else:
        posts = Post.objects.all().order_by("-fecha")

    # Inicializamos el post actual por si no existe una selección válida
    actual_post = None
    post_autor = None
    post_category = None
    post_hashtags = None

    # Definimos el post actual como el seleccionado actual o el último
    if post_id:
        actual_post = Post.objects.get(id = post_id)
    else:
        if len(posts) > 0:
            actual_post = posts[0]
            post_id = actual_post.id
    if actual_post:
        post_autor = actual_post.autor
        post_category = actual_post.categoria
        post_hashtags = Hashtag.objects.filter(post__id = post_id)

    # Construimos el contexto a enviar al HTML
    context = {
        "post_quantity": len(posts),
        "post_list": posts,
        "category_list": categories,
        "hashtag_list": hashtags,
        "actual_post": {
            "post": actual_post,
            "author": post_autor,
            "category": post_category,
            "hashtags": post_hashtags
        },
        "filters": {
            "category_id": int(category_id or 0),
            "hashtag_id": int(hashtag_id or 0)
        }
    }    
    
    # Enviamos a renderizar la pantalla
    return render(request, 'blog.html', context)
