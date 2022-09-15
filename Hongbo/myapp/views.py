from django.shortcuts import render
import pandas as pd
# Create your views here.

def main(request):

    return render(request, 'main.html')

def hmap(request):
    
    return render(request, "hmap.html")

def mapFunc(request):
    
    data = pd.read_csv('/static/csv/popl_7_renew2.csv', encoding='euc-kr')
    print(data.head(3))
    if request.method == 'POST':
        print(data.head(3))
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        
        data_one = data[data['성별'] == gender].nlargest(1, [age])
        x = data_one['위도']
        y = data_one['경도']
        
    return render(request, "hmap.html", {'x':x, 'y':y})
        
def statistics(request):

    return render(request, "statistics.html")

def statisticsFunc(request):
    
    data = pd.read_csv('/csv/month.csv', encoding='euc-kr')
    
    if request.method == 'POST':
        data_statistics = ''
        
    return render(request, "statistics.html" , {'statistics':data_statistics})

