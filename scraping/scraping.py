from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import re
import itertools

page_urls = []
page_soups = []

url = "https://tw.bid.yahoo.com/tw/booth/Y1765779501?userID=Y1765779501&s1=&o1=&catID=&catIDselect=&clf=&at=true&u=:Y1765779501&apg=1#bd"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

# the code below is to get page_urls and page_soups
stop = 0
page = 1
while url:
    page_urls.append(url)
    page_soups.append(soup)
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
things_title = []

for page_soup in page_soups:
    things_title.append(page_soup.find_all('p', attrs={'class':'listing-title'}))
   #print(page_soup.find_all('p', attrs={'class':'listing-title'}))
#print(things_title)

thing_urls = []

for thing in things_title:
    #print(thing)
    for preurl in thing:
        preurl.find('a')
        #print(preurl)
        url_ = re.findall('f="(.*)"', str(preurl))
        #print(url_)
        thing_urls.append(url_)
print(thing_urls)

#GET ALL ITEM SOUP FROM MAIN SITE
#print(thing_urls)
thing_urls = sum(thing_urls,[])


item_soups = []
for url in thing_urls:
    link_res = requests.get(url)
    link_soup = BeautifulSoup(link_res.text,'html.parser')
    item_soups.append(link_soup)
print(len(item_soups))

#FIND TITLE FROM ITEM WEBSITE
thing_titles = []
for str_title in item_soups:
    str_title = str_title.find_all('h1', attrs={'class':'title__3wBva'})
    #print(str_title)
    title = re.findall('《(.*)》', str(str_title))
    #print(title)
    thing_titles.append(title)
    #print(thing_titles)
print(thing_titles)
    

#FIND ALL #TAGS IN ITEM WEBSITE
tag = []
for link_soup in item_soups:
    hashs = link_soup.find_all('a', attrs={'class':'previewDisableAction hashtag__3Usoc'})
#print(page_tag)
    for i in hashs:
        #print(i.text)
        tag.append(i.text)
print(tag)