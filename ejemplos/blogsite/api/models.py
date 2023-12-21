from ninja import Schema
from typing import List


# En este archivo tendremos en vez de modelos de bases de datos
# los esquemas específicos que se utilizan de entrada o salida
# de los servicios.
#
# Recordar que estos esquemas permiten a Django-Ninja convertir
# un diccionario de datos en una estructura JSon o viceversa.

# Este es el esquema utilizado en los mensajes de salida sin datos
class MessageSchema(Schema):
    message: str
    

# Este es el esquema utilizado para la creación de posts exclusivamente
class PostInputSchema(Schema): 
    titulo: str
    texto: str
    autor: int
    categoria: int
    etiquetas: List[int]


# Este es el esquema utilizado para la presentación del autor dentro de un post
class AuthorOutputSchema(Schema):
    id: int
    username: str


# Este es el esquema utilizado para la presentación de la categoría dentro de un post
class CategoryOutputSchema(Schema):
    id: int
    nombre: str


# Este es el esquema utilizado para la presentación de una etiqueta dentro de un post
class HashtagOutputSchema(Schema):
    id: int
    nombre: str


# Este es el esquema utilizado para la presentación de un post, incluyendo los sub-schemas
class PostOutputSchema(Schema): 
    id: int
    titulo: str
    texto: str
    fecha: str
    autor: AuthorOutputSchema
    categoria: CategoryOutputSchema
    hashtags: List[HashtagOutputSchema]