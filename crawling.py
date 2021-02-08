import selenium
import requests
import openpyxl
import re
import os
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


def search(name):
    url = "https://www.google.com/search?q="+quote_plus(name)+"&sxsrf=ALeKk03SX9Jhg9uc3ltvdo8QRyGWY0UFuw:1612776251466&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiZlMjc-9nuAhUXM94KHavQAFsQ_AUoAnoECAIQBA&cshid=1612776392363857&biw=1536&bih=666"
    headers = {"User-Agent":"Chrome/66.0.3359.181"}
    # print(url)
    req = urllib.request.Request(url, headers=headers)
    html = urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.findAll('img')
    imgs = imgs[1:]
    n = 0
    print(imgs)
    for img in imgs:
        imgUrl = img['src']
        file_name = imgUrl.split('/')[-1]
        print(file_name)
        with urlopen(imgUrl) as f:
            os.makedirs(os.path.dirname('images/'+name+'/'+ str(n)+".jpg"), exist_ok=True)
            with open('images/'+name+'/'+ str(n)+".jpg", 'wb') as h:  # w - write b - binary
                img = f.read()
                # print(img)
                h.write(img)
        n += 1
        if n == 2:
            print("done")
            break

