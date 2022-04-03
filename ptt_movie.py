#爬取ppt電影版標題

import requests
from bs4 import BeautifulSoup

def ptt_craweler(page_num=10):
    ptt = 'https://www.ptt.cc'
    url = 'https://www.ptt.cc/bbs/movie/index.html'
    count = page_num
    while count > 0:
        print("---------------第{}頁-----------------".format(page_num-count+1))
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        titles = soup.find_all('div',class_='title')
        for t in titles:
            print(t.text.strip())
        last_link = soup.select_one('a.btn.wide').next_sibling.next_sibling # 只用一個next_sibling會得到'\n'
        url = ptt + last_link['href'] #更新網址
        count -= 1  
    
if __name__ == '__main__':
    ptt_craweler(page_num=8)
