from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def temp(request):
    return render(request, 'indextemp.html', {})

def test(request):
    return render(request, 'index3.html', {})