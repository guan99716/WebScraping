import requests
from bs4 import BeautifulSoup
import json 

url="https://news.ltn.com.tw/list/breakingnews"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

soup1=soup.find("div","whitecon boxTitle")

#宣告一個[字典]資料型態
news={}
infos = soup1.find_all("li")
for info in infos:
    try:    #以標題做為[key]，時間與超連結作為[value]
        key=info.a["title"].strip()
        value1=info.span.text.strip()
        value2=info.a["href"].strip()
        news[key]=[value1,value2]
    except:
        continue
    
#print(newS)        

#顯示[key]值的兩種方法
#print(newS.keys())
#for keY in newS.keys():
#    print(keY)

#顯示[value]值的兩種方法
#print(newS.values())        
#for valuE in newS.values():
#    print(valuE)




#使用[items]搭配[for...in]可以一項項取出[key]與[value]
#for keY,valuE in newS.items():
#    print(keY)
#    print(valuE[0])    
#    print(valuE[1])    

with open("ltnnews.json","w",encoding="utf-8") as file:
    json.dump(news,file,ensure_ascii=False,indent=4)


# 查看json檔裡的內容
with open("ltnnews.json","r",encoding="utf-8") as file:
    ltnNews=json.load(file)

for item in ltnNews.items():
    print(item)  #type(item) == tuple
    print("-"*30)
# print(type(ltnNews))
