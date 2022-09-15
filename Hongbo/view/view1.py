from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect

def board(request):
    return render(request, 'board.html')

def insert(request):
    return render(request, 'insert.html')

def insertok(request):        
    return HttpResponseRedirect('/board/list') 
    

def search(request):         
    return render(request, 'board.html')


def content(request):
    return render(request, 'content.html')
    

def update(request):       
    return render(request, 'update.html')

def updateok(request):
    return render(request, 'update.html')
        
def delete(request):
    return render(request, 'delete.html')

def deleteok(request):
    return redirect('/board/list')  



