from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):
    publicaciones = Entry.objects.all().order_by('-fecha').values()
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'diary.html', context)

