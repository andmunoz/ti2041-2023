from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    
    if request.POST:
        myNumber = int(request.POST['myNumber'])
        myAnswer = myNumber + 1
        context = {
            'myNumber': myNumber,
            'myAnswer': myAnswer
        }

    return render(request, 'index.html', context)