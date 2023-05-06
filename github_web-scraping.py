import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/topics/3d"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

# Getting project topic name

project = soup.find_all("a", class_ = "text-bold wb-break-word")

project_list = []
for i in project:
    data = i.text.strip()
    project_list.append(data)

# Getting username of the project topic
username = soup.find_all("h3", class_= "f3 color-fg-muted text-normal lh-condensed")

username_list = []
for i in username:
    data = i.find_all('a')
    d = data[0].text.strip()
    username_list.append(d)

# Getting Number of stars for projects

stars = soup.find_all("span", id= "repo-stars-counter-star")

star_list = []
for i in stars:
    data = i.text
    star_list.append(data)

# Getting project description 

description = soup.find_all("p", class_= "color-fg-muted mb-0")

description_list = []
for i in description:
    data = i.text
    description_list.append(data)


df = pd.DataFrame({"ProjectName": project_list, "UserName": username_list, "Stars": star_list, "Description":description_list})
df.to_excel("Github_data.xlsx")