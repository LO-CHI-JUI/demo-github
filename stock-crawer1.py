# %% [markdown]
# #抓取goodinfo!台灣股市資訊網- 成交價排行前100名表格資料:

# %% [markdown]
# ###利用get對網站發起請求:

# %%
import requests
url='https://goodinfo.tw/tw/index.asp'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
res=requests.get(url,headers=headers)
res.encoding='utf-8'
print(res.text)

# %% [markdown]
# ###抓取網站中'成交價排行前100名'的表格資料:
# 1. 利用pandas抓取網站中所有表格資料
# 2. 利用迴圈和正則表達式抓取表格第一格第一列內容為'5274 信驊'表格的順位
# 3. 把表格的欄位名稱做修正

# %%
import pandas as pd
import re
df=pd.read_html(res.text)
n=0
for data in df:
    if re.search('5274\s信驊',str(data.iloc[[0],[0]])):
        break
    n+=1
df[n].columns=[u'股票名稱',u'股價',u'漲跌',u'(%)',u'量(張)',u'排名']
print(df[n])

# %% [markdown]
# ###把表格資料存成excel和csv檔，並存，並存入'作業8'資料夾

# %%
import os
if os.path.exists('.\作業8')==False:
    os.mkdir('.\作業8')
df[n].to_excel(r'.\作業8\成交價排行前100名.xlsx')
df[n].to_csv(r'.\作業8\成交價排行前100名.csv')