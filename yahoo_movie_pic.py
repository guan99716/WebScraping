import requests, os
from bs4 import BeautifulSoup

dir = '本週新片'
if not os.path.exists(dir):
  os.mkdir(dir)

url="https://movies.yahoo.com.tw/movie_thisweek.html"
res = requests.get(url)
# print(res.text)
soup=BeautifulSoup(res.text,"lxml")
ul = soup.select('ul.release_list')[0]
for img in ul.find_all('img'):
  img_link = img.get('data-src')
  pic = requests.get(img_link)
  fn = img_link.split('/')[-1]
  with open(dir + '\\' + fn,'wb') as f:
    for d in pic.iter_content():
      f.write(d)
    print('已下載:',fn)