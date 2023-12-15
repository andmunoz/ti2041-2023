from ninja import NinjaAPI, Redoc
from blog.models import Post, Category, Hashtag
from django.contrib.auth.models import User
from .models import PostInputSchema, PostOutputSchema, HashtagOutputSchema, MessageSchema
from typing import List

# Creamos un objeto para manipular la API
api = NinjaAPI(docs=Redoc(), title="Documentación para el Blog", version="1.0.0", description="Esta es la documentación de la API para el ejemplo del Blog")


# Servicio dummy solo para comprobar que la API funciona
@api.get("dummy", response={200:MessageSchema}, summary="Servicio de pruebas de acceso a la API")
def get_dummy(request):
    """
    Devuevlve un mensaje "hello world" como pruebas
    """

    results = { 'message': 'hello world' }
    return results


# Servicio que obtiene TODOS los posts de la base de datos
# En este caso solo se tiene 1 respuesta posible: Staus 200 (una lista de posts)
@api.get("post", response={200:List[PostOutputSchema]}, summary="Servicio que obtiene todos los artículos del blog")
def get_posts(request):
    """
    Devuevlve una lista con la información de todos los artículos almacenados en el sistema
    """

    # Se obtienen todos los Post desde el modelo
    posts = Post.objects.all().order_by("fecha")
    
    # Creamos un resultado vacío (en este caso, una lista)
    results = []
    
    # Iteramos por cada post
    for post in posts:
        # Creamos el objeto que representa cada post de resultado
        # En este caso se debe respetar la estructura y tipos del schema
        # PostOutputSchema del archivo models.py
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
    
        # Para construir la lista de tags, se debe hacer aparte, ya que es una lista de objetos
        # que debe respetar la estructura y tipos del schema HashtagOutputSchema
        for etiqueta in post.etiquetas.all():
            hashtag = {
                "id": etiqueta.id, 
                "nombre": etiqueta.nombre,
            }
            result["hashtags"].append(hashtag)
            
        # Se guarda en la lista de resultados
        results.append(result)
        
    # Se devuelve la lista de post con los resultados
    return results


# Servicio que obtiene un post en particular desde la base de datos
# En este caso, se tienen 2 respuestas posibles: Status 200 y Error 404
@api.get("post/{id}", response={200:PostOutputSchema, 404:MessageSchema}, summary="Servicio que obtiene un artículo en particular")
def get_post(request, id):
    """
    Devuevlve un objeto con toda la información del artículo ingresado. 
    """

    # Se consulta por el post en el modelo, si ocurre un error, es porque el id no existe
    try: 
        post = Post.objects.get(id=id)
    except Exception:
        return 404, { 'message': 'Post not found' }
    
    # Creamos el objeto que representa el post de resultado
    # En este caso se debe respetar la estructura y tipos del schema
    # PostOutputSchema del archivo models.py
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
    
    # Para construir la lista de tags, se debe hacer aparte, ya que es una lista de objetos
    # que debe respetar la estructura y tipos del schema HashtagOutputSchema
    for etiqueta in post.etiquetas.all():
        hashtag = {
            "id": etiqueta.id, 
            "nombre": etiqueta.nombre,
        }
        result["hashtags"].append(hashtag)
        
    # Se devuelve el post con el resultado
    return result
    
    
# Servicio que crea un post en la base de datos
# En este caso, se tienen 2 respuestas posibles: Status 200 y Error 404
@api.post("post", response={200:MessageSchema, 404:MessageSchema}, summary="Servicio crea un artículo")
def save_post(request, p: PostInputSchema):
    """
    Crea un artículo en el sistema a partir de la información enviada
    """
    
    # Primero se valida que el autor exista
    try: 
        author = User.objects.get(id=p.autor)
    except Exception:
        return 404, { 'message': 'Author not found' }
    
    # Luego se valida que la categoría exista
    try: 
        category = Category.objects.get(id=p.categoria)
    except Exception:
        return 404, { 'message': 'Category not found' }
    
    # Finalmente se crea la lista de etiquetas asociadas al post
    hashtags = []
    for etiqueta in p.etiquetas:
        try:
            hashtag = Hashtag.objects.get(id=etiqueta)
        except Exception:
            return 404, { 'message': 'A hashtag not found' }
        hashtags.append(hashtag)
    
    # Se crea la estructura de objeto a crear en el modelo
    post = {
        "titulo": p.titulo,
        "texto": p.texto,
        "autor": author,
        "categoria": category
    }

    # Se crea el objeto directamente y se persiste    
    post = Post.objects.create(**post)
    post.save()

    # Se asocian los hashtag al post
    for hashtag in hashtags:        
        post.etiquetas.add(hashtag)
        post.save()
    
    # Se devuelve un mensaje de que se ha realizado correctamente la operación
    return { 'message': 'Post has been created' }


# Servicio que crea un post en la base de datos
# En este caso, se tienen 2 respuestas posibles: Status 200 y Error 404
@api.delete("post/{id}", response={200:MessageSchema, 404:MessageSchema}, summary="Servicio que elimina un artículo")
def delete_post(request, id: int):
    """
    Elimina un artículo del sistema a partir de la información enviada
    """

    # Se valida que el artículo exista
    try: 
        post = Post.objects.get(id=id)
    except Exception:
        return 404, { 'message': 'Post not found' }
    
    # Se elimina el objeto del modelo
    post.delete()
    
    # Se devuelve un mensaje de que se ha realizado correctamente la operación
    return { 'message': 'Post has been deleted' }