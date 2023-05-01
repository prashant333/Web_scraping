import requests
from bs4 import BeautifulSoup

link = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r= requests.get(link)

soup = BeautifulSoup(r.text, "lxml")

prices = soup.find_all("h4", class_ = "pull-right price")
# print(type(prices))

for i in prices:
    print(i.string)

