from django.shortcuts import render
import pandas as pd
import random
import openpyxl

# Create your views here.

def main(request):
    data = pd.read_csv("https://raw.githubusercontent.com/3307rla/Hongbo/main/Hongbo/myapp/static/csv/%ED%8C%90%EC%B4%89%EB%AC%BC%EC%97%85%EC%B2%B4.csv", encoding='euc-kr')
    # data = pd.read_excel("C:/Users/acorn/Desktop/Hongbo2/Hongbo/Hongbo/myapp/static/판촉물업체.xlsx")
    ndata = data[['LABEL-1', 'LABEL-3', 'site']]
    ndata.columns = ['이름', '주소', '사이트']
    
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

def statistics(request):

    return render(request, "statistics.html")

