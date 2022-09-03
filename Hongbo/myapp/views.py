from django.shortcuts import render

# Create your views here.

def mainFunc(request):

    return render(request, 'main.html')

def index(request):

  return render(request, "index.html")
