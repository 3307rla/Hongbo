from django.shortcuts import render, redirect

def reply(request):
        return render(request, 'rep/reply.html')

def replyok(request):
            return redirect('/board/list') 



