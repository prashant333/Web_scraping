import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/market"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find_all("table", class_ = "table table-sm table-hover screenertable")[2]

header = table.find_all("th")
header_list =[]

for i in header:
    data = i.text
    header_list.append(data)
#print(header_list)

df = pd.DataFrame(columns = header_list)
#print(df)

rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [i.text for i in data]
    l = len(df)
    df.loc[l] = row
    df['Company'] = df['Company'].apply(lambda x:x.strip())
print(df)

#df.to_excel("scrap_table.xlsx")