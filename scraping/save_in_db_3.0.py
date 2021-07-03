from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import re
import itertools
import pymysql

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "project",
    "charset": "utf8"
}

page_urls = []
page_soups = []
titles = [""]
tags = []
pic_urls = []

url = "https://tw.bid.yahoo.com/tw/booth/Y1765779501?userID=Y1765779501&s1=&o1=&catID=&catIDselect=&clf=&at=true&u=:Y1765779501&apg=1#bd"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

# the code below is to get page_urls and page_soups
stop = 0
page = 0

results = list()
while url:
    
    results = list()
    
    page = page + 1
    #print(page)
    url = "https://tw.bid.yahoo.com/tw/booth/Y1765779501?userID=Y1765779501&s1=&o1=&catID=&catIDselect=&clf=&at=true&u=:Y1765779501&apg=" + str(page) + "#bd"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    bds = soup.find_all("div",class_="bd")
    
    
    for bd in bds:
        ps = bd.find_all("p")
        for p in ps:
            if p.text == "沒有可供預覽的縮圖。":
                stop = 1   
    if stop == 1:
        break
    
    title = soup.find_all('p', attrs={'class':'listing-title'})
        
        
    for preurl in title:
        preurl.find('a')
        url_ = re.findall('f="(.*)"', str(preurl))
        #print(url_)

        #pull down soup from url_
        link_res = requests.get(url_[0])
        link_soup = BeautifulSoup(link_res.text,'html.parser')

        #find title from link_soup
        str_title = link_soup.find_all('h1', attrs={'class':'title__3wBva'})
        title = re.findall('《(.*)》', str(str_title))
        titles.append(title)

        if len(title) == 1:

            ttt = title[0]
            #print(ttt)


            #find hash form link_soup
            #tmp = []
            hashs = link_soup.find_all('a', attrs={'class':'previewDisableAction hashtag__3Usoc'})

            #print(hashs)
            tags = ['' for i in range(8)]
        
            tags[0] = ttt
        
            for i, j in enumerate(i.getText().strip('#') for i in hashs):
                tags[i+1] = j
                #print(tags)
            tuple(tags)
            #print(type(ttt))
            #print(tags)
        

            pics = []
            img = link_soup.find_all('li', attrs={'class':'listItem__3BRt8'})
            for img in img:
                img.find_all('img')
                pic_url = re.findall('src="(.*)"', str(img))
                #print(pic_url)
                pics.append(pic_url)
            pic_urls.append(pics)


            goods = [] 
            for tag in tags:
                goods.append(tag)

            for pi in pics:
                for pii in pi:
                    goods.append(pii)    
        
            while len(goods) < 38:
                goods.append('')
            tuple(goods)
            print(goods)
            conn = pymysql.connect(**db_settings)

            with conn.cursor() as cursor:
                sql = """INSERT INTO merchandize(name, hashtag1, hashtag2, hashtag3, hashtag4, hashtag5, hashtag6, hashtag7, pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9, pic10, pic11, pic12, pic13, pic14, pic15, pic16, pic17, pic18, pic19, pic20, pic21, pic22, pic23, pic24, pic25, pic26, pic27, pic28, pic29, pic30) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(sql, goods)
                conn.commit()