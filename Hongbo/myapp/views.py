from django.shortcuts import render
import pandas as pd
import random
import json
# Create your views here.

def main(request):
    data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/%ED%8C%90%EC%B4%89%EB%AC%BC%EC%97%85%EC%B2%B4.csv", encoding='euc-kr')
    ndata = data[['LABEL-1', 'LABEL-3', 'site', 'img']]
    ndata.columns = ['이름', '주소', '사이트', '이미지']
        
    li = random.sample(range(0,48),9)
    
    df = ndata.iloc[li]
    
    dict = {}
    
    for i in range(len(li)):
        dict['dict'+str(i)] = {
            '이름':df.iloc[i].이름,
            '주소':df.iloc[i].주소,
            '사이트':df.iloc[i].사이트,
            '이미지':df.iloc[i].이미지
            }
    
    return render(request, 'main.html', {'dict':dict})

def hmap(request):
    

    return render(request, "hmap.html")

def mapFunc(request):
    
    data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/popl_7_renew2.csv", encoding='euc-kr')

    if request.method == 'POST':
        
        mapdata = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/popl_7_renew2.csv", encoding='euc-kr')
        
        mapdata.set_index("시군구", inplace=True)
        
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        time = request.POST.get('time')
        
        data_one = mapdata[(mapdata['성별'] == gender) & (mapdata['시간대구분'] == 14)].nlargest(4, [age], keep='first')
        x = data_one[['위도']]
        y = data_one[['경도']]
        
        x1 = x.iloc[[1]].values[0, 0]
        x2 = x.iloc[[2]].values[0, 0]
        x3 = x.iloc[[3]].values[0, 0]
        
        y1 = y.iloc[[1]].values[0, 0]
        y2 = y.iloc[[2]].values[0, 0]
        y3 = y.iloc[[3]].values[0, 0]
        
    return render(request, "hmap.html", {'x1':x1, 'x2':x2, 'x3':x3, 'y1':y1, 'y2':y2, 'y3':y3})

        
def statistics(request):
    
    df = pd.read_csv('https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/ingu.csv', encoding='euc-kr')
    
    Q = []

    for i in range(df.shape[0]):
        Q.append([])
        for j in range(2, 8):
            Q[i].append(float(df.iloc[i, [j]]))
    
    df = df.drop([f'{i}월' for i in range(2, 8)], axis=1)
    df['graph'] = Q
    
    df = pd.DataFrame(df)
    
    json_records = df.reset_index().to_json(orient='records')
    data = []
    data = json.loads(json_records)
    context = {'d':data}

    return render(request, "statistics.html", context)

