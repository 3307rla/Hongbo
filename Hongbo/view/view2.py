from django.shortcuts import render, redirect
from myapp.models import BoardTab
from datetime import datetime
from django.http.response import HttpResponseRedirect

def reply(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))
        context = {'data_one':data}
        return render(request, 'rep/reply.html', context)
    except Exception as e:
        print('댓글 대상 원글 읽기 오류 : ', e)
        return render(request, 'error.html')

def replyok(request):
    if request.method == "POST":
        try:
            # print(request.POST.get('id'), request.POST.get('name'))
            # onum 처리...
            repGnum = int(request.POST.get('gnum'))
            repOnum = int(request.POST.get('onum'))
            imsiRec = BoardTab.objects.get(id=request.POST.get('id'))
            oldGnum = imsiRec.gnum
            oldOnum = imsiRec.onum
            
            if oldOnum >= repOnum and oldGnum == repGnum:
                oldOnum = oldOnum + 1            
            
            # 댓글 저장
            BoardTab(
                name = request.POST.get('name'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bdate = datetime.now(),
                readcnt = 0,
                gnum = repGnum,
                onum = oldGnum,
                nested = int(request.POST.get('nested')) + 1,  
            ).save()
            return HttpResponseRedirect('/board')
            
        except Exception as e:
            print('댓글 저장 오류 : ', e)
            return render(request, 'error.html')


