import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

product_name = soup.find_all("a", class_ = "title")

product_list =[]
for i in product_name:
    name = i.text
    product_list.append(name)

product_price = soup.find_all("h4", class_ = "pull-right price")

price_list = []
for i in product_price:
    price = i.text
    price_list.append(price)

product_review = soup.find_all("p", class_ = "pull-right")

review_list = []
for i in product_review:
    review = i.text
    review_list.append(review)

df = pd.DataFrame({"Product Name": product_list, "Price": price_list, "Review": review_list})
# print(df)

# this is will create a file in csv format.
# df.to_csv("Web_scraping_using_pandas.csv")

df.to_excel("webscraping_usingPandas.xlsx")