# this program describes find() function from beautifulsoup library. 
import requests
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

soup = BeautifulSoup(r.text, "lxml")

price = (soup.find("h4", {"class":"pull-right price"}))
print(price.string)

# this is another way of passing a class name
desc = (soup.find("p", class_ = "description"))
print(desc.string)