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


class AuthorOutputSchema(Schema):
    id: int
    username: str


class CategoryOutputSchema(Schema):
    id: int
    nombre: str


class HashtagOutputSchema(Schema):
    id: int
    nombre: str


class PostOutputSchema(Schema): 
    id: int
    titulo: str
    texto: str
    fecha: str
    autor: AuthorOutputSchema
    categoria: CategoryOutputSchema
    hashtags: List[HashtagOutputSchema]