import requests
from bs4 import BeautifulSoup
import csv 

url="https://news.ltn.com.tw/list/breakingnews"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

soup1=soup.find("div","whitecon boxTitle")

csvFile=open("ltnnews.csv","w+",newline="",encoding="utf-8-sig")
writer=csv.writer(csvFile)
writer.writerow(["時間","標題","超連結"])
infos = soup1.find_all("li")
for info in infos:
    try:    #以標題做為[key]，時間與超連結作為[value]
        title=info.a["title"].strip()
        time=info.span.text.strip()
        link=info.a["href"].strip()
        writer.writerow([time,title,link])
    except:
        continue
    
csvFile.close()


