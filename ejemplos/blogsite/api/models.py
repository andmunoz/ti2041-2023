from ninja import Schema
from django.db import models
from typing import List

# Create your models here.

class MessageSchema(Schema):
    message: str
    

class PostInputSchema(Schema): 
    titulo: str
    texto: str
    autor: int
    categoria: int


class HashtagOutputSchema(Schema):
    nombre: str


class PostOutputSchema(Schema): 
    id: int
    titulo: str
    texto: str
    fecha: str
    autor: str
    categoria: str
    # hastags: List[HashtagOutputSchema]