from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from myapp.models import BoardTab

def board(request):
    
    return render(request, 'board.html')

def insert(request):
    return render(request, 'insert.html')

def insertok(request):        
    if request.method == 'POST':
        try:
            gbun = 1  # Group number 구하기
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1
                
            BoardTab(
                name = request.POST.get('name'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0,                
            ).save()
        except Exception as e:
            print('추가 에러 : ', e)
            return render(request, 'error.html')
        
    return HttpResponseRedirect('/board')  # 추가 후 목록보기    

def search(request):         
    return render(request, 'board.html')


def content(request):
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))
    # 조회수 갱신
    data.readcnt = data.readcnt + 1
    data.save()
    return render(request, 'content.html', {'data_one':data, 'page':page}) 

def update(request):       
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
            print('수정 자료 읽기 오류 : ', e)
            return render(request, 'error.html')
        
    return render(request, 'update.html', {'data_one':data})

def updateok(request):
    try:
        upRec = BoardTab.objects.get(id=request.POST.get('id'))
        
        if request.method == 'POST':
    
            name = request.POST.get('name')
            title = request.POST.get('title')
            cont = request.POST.get('cont')
    
            upRec.name = name
            upRec.title = title
            upRec.cont = cont
            upRec.mail = request.POST.get('mail')
    
            upRec.save()
        else:
            return render(request, 'update.html', {'data_one':upRec})
        
    except Exception as e:
            print('수정 처리 읽기 오류 : ', e)
            return render(request, 'error.html')
        
    return HttpResponseRedirect('/board')  # 수정 후 목록보기    

def delete(request):
    return render(request, 'delete.html')

def deleteok(request):
    return HttpResponseRedirect('/board')



