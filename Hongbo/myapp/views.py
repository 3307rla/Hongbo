from django.shortcuts import render

# Create your views here.

def main(request):

    return render(request, 'main.html')

def hmap(request):

    return render(request, "hmap.html")

def statistics(request):

    return render(request, "statistics.html")

