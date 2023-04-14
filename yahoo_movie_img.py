import requests, os
from bs4 import BeautifulSoup

dir_name = 'NewMovies(This_Week)'
if not os.path.exists(dir_name):
  os.mkdir(dir_name)
movie_names=[]
img_links=[]
page = 1
while True:
    url="https://movies.yahoo.com.tw/movie_thisweek.html?page="+str(page)
    res = requests.get(url)
    soup=BeautifulSoup(res.text,"lxml")
    ul = soup.select_one('ul.release_list')
    lis = ul.select('li') 
    for i in range(len(lis)):
        movie_names.append(lis[i].select_one('div.release_movie_name a').text.strip())
        img_links.append(lis[i].find('img').get('data-src'))
    next_page_tag = soup.select_one('.nexttxt a')
    if next_page_tag:
        page+=1
    else:
        break

for name,link in zip(movie_names,img_links):
    img= requests.get(link)
    with open(dir_name + '\\' + name+'.jpg','wb') as f:
        for d in img.iter_content():
            f.write(d)
        print('downloaded:',name)

print('----done-----')
  
      