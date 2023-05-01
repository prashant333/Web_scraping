import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")

table_header = table.find_all("th")

table_header_list = []

for i in table_header:
    data = i.text
    table_header_list.append(data)

df = pd.DataFrame(columns=table_header_list)

rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [i.text for i in data]
    l = len(df)
    df.loc[l] = row
    df["TEAM"] = df["TEAM"].apply(lambda x:x.strip())
print(df)

df.to_excel("IPL_auction_sheet.xlsx")