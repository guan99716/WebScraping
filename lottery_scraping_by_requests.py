# requests
# 表單填入, 爬取某年某月的威力彩球號
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import os
import time
def lottery2(year,month):
    res = requests.get('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx')
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        __VIEWSTATE = soup.find('input',id='__VIEWSTATE')
        __VIEWSTATEGENERATOR = soup.find('input',id='__VIEWSTATEGENERATOR')
        __EVENTVALIDATION = soup.find('input',id='__EVENTVALIDATION')

    lottery_data = {'__VIEWSTATE': __VIEWSTATE.get('value'),
                '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR.get('value'),
                '__EVENTVALIDATION': __EVENTVALIDATION.get('value'),
                'forma': '請選擇遊戲',
                'SuperLotto638Control_history1$txtNO':'',
                'SuperLotto638Control_history1$chk': 'radYM',
                'SuperLotto638Control_history1$dropYear': str(year),
                'SuperLotto638Control_history1$dropMonth': str(month),
                'SuperLotto638Control_history1$btnSubmit': '查詢'
    }

    res = requests.post('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',data=lottery_data)
    if res.status_code == 200:
        #print(r.text)
        soup = BeautifulSoup(res.text,'html.parser')
    #     by using regex
        data = soup.find_all('span',id = re.compile('SuperLotto638Control_history1_dlQuery_SNo\d_\d'))
        ball_nums = [num.text for num in data]
        ball_array = np.array(ball_nums)
        ball_array = ball_array.reshape(len(ball_nums)//7,7)
        df = pd.DataFrame(ball_array)
        df.columns = ['第1號','第2號','第3號','第4號','第5號','第6號','特別號']
        df.to_csv('ball_nums2/lottery{}_{}.csv'.format(year,month),encoding='utf8') # or use cp950
        print('已下載{}年{}月的資料'.format(year,month))

if __name__ == '__main__':
    if not os.path.exists('ball_nums2'):
        os.mkdir('ball_nums2')
    for i in range(1,13):
        lottery2(104,i)
        time.sleep(1)
        
    print('----下載完畢----')
