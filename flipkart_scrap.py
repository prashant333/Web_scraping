import requests
import pandas as pd
from bs4 import BeautifulSoup

name_list = []
price_list = []
rating_list = []
desc_list = []

for i in range(1,21):

    url = "https://www.flipkart.com/search?q=mobile%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"+str(i)

    r = requests.get(url)
    print(r)

    soup = BeautifulSoup(r.text, "lxml")


    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    name = box.find_all("div", class_ = "_4rR01T")

    for i in name:
        data = i.text
        name_list.append(data)


    price = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in price:
        data = i.text
        price_list.append(data)

    rating = box.find_all("div", class_= "_3LWZlK")

    for i in rating:
        data = i.text
        rating_list.append(data)

    desc = box.find_all("ul", class_ = "_1xgFaf")

    for i in desc:
        data = i.text
        desc_list.append(data)
df = pd.DataFrame({"Mobile_Name": name_list, "Cost":price_list, "Description":desc_list, "Rating":rating_list,})
df.to_csv("Flipkart_mobile_dump.csv")
