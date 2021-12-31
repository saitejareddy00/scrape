import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getf_url(r):
    p="https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    r=r.replace(' ','+')
    url=p.format(r)
    #url+='&page{}'
    return url

def get_url(r):
    p="https://www.amazon.in/s?k={}&ref=nb_sb_noss_1"
    r=r.replace(' ','+')
    url=p.format(r)
    url+='&page{}'
    return url

def extract_record(item):
    at=item.h2.a
    name=at.text.strip()
    url="https://www.amazon.in"+at.get('href')

    try:
        price_p=item.find('span','a-price')
        price=price_p.find('span','a-offscreen').text
    except AttributeError:
        price=''
        
    try:
        rating=item.i.text
    except AttributeError:
        rating=''

    try:
        rc=item.find('span','a-size-base').text
    except AttributeError:
        rc=''

    return [name,price,rating,rc,url]
def finalfunc(search):
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
    
    ide_ra=[]
    url=get_url(search)

    '''for i in range(1,21):'''
    driver.get(url.format(1))
    soup=BeautifulSoup(driver.page_source,'html.parser')
    results=soup.find_all('div',{'data-component-type':'s-search-result'})
    for i in range(5):
        ide_ra.append(extract_record(results[i]))
    n=[]
    print(len(ide_ra))
    for i in range(5):
        n.append(ide_ra[i][0])
    for i in n:
        print(i)
    '''for i in range(5):
        chk=st.checkbox(ide_ra[i][0])
        if chk:
            st.write(ide_ra[i][1],ide_ra[i][2],ide_ra[i][3])'''
    pls=[]
    
    for i in n:
        if '%' in i:
            i=i.replace('%','')
        if '!' in i:
            i=i.replace('!','')
        url=getf_url(i)
        driver.get(url)
        soup=BeautifulSoup(driver.page_source,'html.parser')

        try:
            parent=soup.find('div',{'class':'_1YokD2 _3Mn1Gg'})
            r1=parent.findChildren("div",recursive=False)
            r2=r1[1].findChildren("div",recursive=False)
            r3=r2[0].findChildren("div",recursive=False)
            #for j in r3:
            r4=r3[0].findChildren("div",recursive=False)
            r5=r4[0].findChildren("a",recursive=False)
            pls.append("https://www.flipkart.com"+r5[0].get('href'))
        except:
            pls.append("")
    hush=[]
    for i in pls:
        if i=="":
            name="Unavailable"
            price=""
            rating=""
            rc=""
            hush.append([price,rating,rc,i])
            continue

        if 'GROCERY' in i:
            ind=pls.index(i)
            u=getf_url(n[ind])
            if '%' in u:
                u=u.replace('%','')
            if '!' in u:
                u=u.replace('!','')
            driver.get(u)
            soup=BeautifulSoup(driver.page_source,'html.parser')

            try:
                price=soup.find('div',{'class':'_30jeq3'})
                price=price.text
            except AttributeError:
                price=''

            try:
                rating=soup.find('div',{'class':'_3LWZlK'})
                rating=rating.text
            except AttributeError:
                rating=''

            try:
                rc=soup.find('span',{'class':'_2_R_DZ'})
                rc=rc.text
            except AttributeError:
                rc=''

        else:
            driver.get(i)
            soup=BeautifulSoup(driver.page_source,'html.parser')

            try:
                price=soup.find('div',{'class':'_30jeq3 _16Jk6d'})
                price=price.text
            except AttributeError:
                price=''

            try:
                parent=soup.find('div',{'class':'_3_L3jD'})
                r1=parent.findChildren("div",recursive=False)
                r2=r1[0].findChildren("span",recursive=False)
                r3=r2[0].findChildren("div",recursive=False)
                rating=r3[0].text
            except AttributeError:
                rating=''

            try:
                r4=r2[1].findChildren("span",recursive=False)
                r5=r4[0].findChildren("span",recursive=False)
                rc=r5[0].text
            except:
                rc=''

        hush.append([price,rating,rc,i])
    
    
    
    driver.close()
    return ide_ra,hush,True
