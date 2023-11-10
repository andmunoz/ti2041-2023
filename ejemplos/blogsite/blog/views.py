from django.shortcuts import render
from .models import Post, Hashtag

# Create your views here.
def index(request, id = None):
    posts = Post.objects.all().order_by("-fecha")
    actual_post = None

    if id:
        actual_post = Post.objects.get(id = id)
    else:
        actual_post = posts[0]
        id = actual_post.id
    category = actual_post.categoria
    hashtags = Hashtag.objects.filter(post__id = id)

    context = {
        "actual_post": {
            "post": actual_post,
            "categpry": category,
            "hashtags": hashtags
        },
        "post_list": posts
    }    

    print(context)
    return render(request, 'index.html', context)
