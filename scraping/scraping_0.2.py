from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import re
import itertools



page_urls = []
page_soups = []
titles = []
tags = []
pic_urls = []

url = "https://tw.bid.yahoo.com/tw/booth/Y1765779501?userID=Y1765779501&s1=&o1=&catID=&catIDselect=&clf=&at=true&u=:Y1765779501&apg=1#bd"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

# the code below is to get page_urls and page_soups
stop = 0
page = 1
while url:
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
        #print(title)
        
        
        #find hash form link_soup
        tmp = []
        hashs = link_soup.find_all('a', attrs={'class':'previewDisableAction hashtag__3Usoc'})
        for i in hashs:
            print(i.text)
            tmp.append(i.text)
        tags.append(tmp)
        

        pics = []
        img = link_soup.find_all('li', attrs={'class':'listItem__3BRt8'})
        for img in img:
            img.find_all('img')
            pic_url = re.findall('src="(.*)"', str(img))
            #print(pic_url)
            pics.append(pic_url)
        pic_urls.append(pics)


