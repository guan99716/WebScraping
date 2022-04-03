# 爬取某年某月的威力彩球號

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import os

def lottery(year,month):
    driver.find_element(By.ID,'SuperLotto638Control_history1_radYM').click()
    select1 = Select(driver.find_element(By.ID,'SuperLotto638Control_history1_dropYear'))
    select1.select_by_value(str(year))
    select2 = Select(driver.find_element(By.ID,'SuperLotto638Control_history1_dropMonth'))
    select2.select_by_value(str(month))
    # search_click
    driver.find_element(By.ID,'SuperLotto638Control_history1_btnSubmit').click()

    soup = BeautifulSoup(driver.page_source,'lxml')
    id_rex = re.compile(r'SuperLotto638Control_history1_dlQuery_SNo._.')
    balls = soup.find_all('span',id=id_rex)
    balls = np.array([b.text for b in balls])
    balls = balls.reshape(len(balls)//7,7)
    df = pd.DataFrame(balls)
    df.columns = ['第1號','第2號','第3號','第4號','第5號','第6號','特別號']
    
    df.to_csv('ball_nums/lottery{}_{}.csv'.format(year,month),encoding='cp950')
    print('已下載{}年{}月的資料'.format(year,month))

# for example: 104年1-12月資料
if __name__ == '__main__':
    if not os.path.exists('ball_nums'):
        os.mkdir('ball_nums')
    driver = webdriver.Chrome()
    url = 'https://www.taiwanlottery.com.tw/Lotto/SuperLotto638/history.aspx'
    driver.get(url)
        
    for i in range(1,13):
        lottery(104,i)
    print(----下載完畢----)
    driver.quit()