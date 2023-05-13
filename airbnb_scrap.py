import requests
import pandas as pd
from bs4 import BeautifulSoup

Name_list = []
price_list = []
rating_list = []
desc_list = []

url = "https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"

r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")

count = 0
while count < 15:
    Name = soup.find_all("div", class_= "t1jojoys dir dir-ltr")
    for i in Name:
        data = i.text
        Name_list.append(data)
    print(len(Name_list))
    price = soup.find_all("div", class_= "_1jo4hgw")
    for i in price:
        data = i.text
        price_list.append(data)
    print(len(price_list))
    rating = soup.find_all("span", class_ = "r1dxllyb dir dir-ltr")

    for i in rating:
        data = i.text
        rating_list.append(data)
    print(len(rating_list))

    try:
        np = soup.find("a", class_= "c1ytbx3a").get("href")
        next_page = "https://www.airbnb.co.in"+np
        #print(next_page)
    except:
        print("This was last page.")


    url = next_page
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    count +=1


df = pd.DataFrame({"Hotel_Name":Name_list, "Cost":price_list, "Rating":rating_list})
df.to_json("Airbnb_data.json")
