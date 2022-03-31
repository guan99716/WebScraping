import pandas as pd
def currency_crawler():
    df = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')[0]
    df1 = df.drop(columns=[('即期匯率','本行賣出'),('即期匯率','Unnamed: 6_level_1')]).dropna(axis=1)
    df2 = df1.iloc[:,:-4]
    df2.columns = ['幣別','現金買入','現金賣出','即期買入','即期賣出']
    df2['幣別'] =[s[:len(s)//2-1] for s in list(df2['幣別'])]
#     df2['幣別'] = ['美金 (USD)', '港幣 (HKD)', '英鎊 (GBP)', '澳幣 (AUD)', '加拿大幣 (CAD)', '新加坡幣 (SGD)', '瑞士法郎 (CHF)', '日圓 (JPY)', '南非幣 (ZAR)', '瑞典幣 (SEK)', '紐元 (NZD)', '泰幣 (THB)', '菲國比索 (PHP)', '印尼幣 (IDR)', '歐元 (EUR)', '韓元 (KRW)', '越南盾 (VND)', '馬來幣 (MYR)', '人民幣 (CNY)']
    df2.to_csv('currency.csv')
if __name__ == '__main__':
    currency_crawler()