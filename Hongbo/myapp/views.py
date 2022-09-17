from django.shortcuts import render
import pandas as pd
import random
import json
# Create your views here.

def main(request):
    data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/%ED%8C%90%EC%B4%89%EB%AC%BC%EC%97%85%EC%B2%B4.csv", encoding='euc-kr')
    ndata = data[['LABEL-1', 'LABEL-3', 'site']]
    ndata.columns = ['이름', '주소', '사이트']
    # print(ndata.iloc[[0,1,3,5]])
    li = []
    for i in range(9):
        num = random.randint(0, 52)
        # print(num)
        li.append(num)
    
    df = ndata.iloc[li]
    print(df)
    
    dict = {}
    
    for i in range(len(li)):
        dict['dict'+str(i)] = {
            '이름':df.iloc[i].이름,
            '주소':df.iloc[i].주소,
            '사이트':df.iloc[i].사이트
            }
    
    return render(request, 'main.html', {'dict':dict})

def hmap(request):
    
    return render(request, "hmap.html")

def mapFunc(request):
    
    data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/popl_7_renew2.csv", encoding='euc-kr')
    print(data.head(3))
    if request.method == 'POST':
        data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/popl_7_renew2.csv", encoding='euc-kr')
        print(data.head(3))
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        
        data_one = data[data['성별'] == gender].nlargest(1, [age])
        x = data_one['위도']
        y = data_one['경도']
        
    return render(request, "hmap.html", {'x':x, 'y':y})
        
def statistics(request):
    df = pd.read_csv('hongbo/myapp/static/csv/ingu.csv', encoding='cp949')
    
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
