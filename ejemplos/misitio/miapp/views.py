from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        yourNumber = int(request.POST.get('numero', '0'))
        myNumber = yourNumber + 1
        return render(request, "jalisco.html", {'yourNumber':yourNumber, 'myNumber':myNumber})
    return render(request, "jalisco.html")
 