url = 'https://news.ltn.com.tw/list/breakingnews'
# title time link
import requests 
import pandas as pd
from bs4 import BeautifulSoup

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
# 只能爬到第1頁, 其他頁需要下滑，要使用JS (所以要用Selenium)
infos = soup.find_all('li',{"data-page":1})
result = []
for info in infos:
    try:
        time = info.select_one('span.time').text
        title = info.select_one('a.ph.listS_h')['title']
        link = info.select_one('a.ph.listS_h')['href']
        result.append([time, title, link])
        # 有時候要用strip把左右空白去掉
    except:
        continue
df = pd.DataFrame(result,columns=['time','title','link'])
df.to_csv('ltn.csv')