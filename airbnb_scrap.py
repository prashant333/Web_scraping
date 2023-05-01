import requests
import pandas as pd
from bs4 import BeautifulSoup

header_list = []
price_list = []
rating_list = []
desc_list = []

url = "https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"

r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")

while True:
    np = soup.find("a", class_= "c1ytbx3a").get("href")
    next_page = "https://www.airbnb.co.in"+np
    print(next_page)

    url = next_page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")


#box = soup.find("div", class_="l196t2l1 dir dir-ltr")
#
#header = box.find_all("div", class_= "t1jojoys")
#
#for i in header:
#    data = i.text
#    header_list.append(data)
#print(header_list)
#
#price = box.find_all("div", class_= "_1jo4hgw")
#
#for i in price:
#    data = i.text
#    price_list.append(data)

#print(price_list)
