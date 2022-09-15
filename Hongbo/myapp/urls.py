from django.urls import path
from view import view1, view2

urlpatterns = [

    path('', view1.board, name='board'),
    
    path('insert', view1.insert),
    path('insertok', view1.insertok),
    
    path('search', view1.search),
    
    path('content', view1.content),
    
    path('update', view1.update),
    path('updateok', view1.updateok),
    
    path('delete', view1.delete),
    path('deleteok', view1.deleteok),
    
    # 댓글(답글)
    path('reply', view2.reply),
    path('replyok', view2.replyok),

]
