import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
playerList=[]
page = requests.get("https://www.atptour.com/en/rankings/singles")
soup = BeautifulSoup(page.content, 'html.parser')
table_body=soup.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    playerList.append(cols)
    #print(cols)

print(playerList)
file = open('rankingTable.csv', 'w+', newline='')

# writing the data into the file
with file:
    header = ['Ranking', 'Move', 'Country','Player','Age','Points','Tournament_Played','Points_Dropping','Next_best']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    write = csv.writer(file)
    write.writerows(playerList)
