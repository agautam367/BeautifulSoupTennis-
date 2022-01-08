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
listPlayers=[]
x= len(soup.select('.player-cell a'))
player=soup.select('.player-cell a')
for i in range(0,x-1):
    if(player[i]['ga-label']!="TopCourt"):
        #print(player[i]['ga-label'])
        listPlayers.append(player[i]['ga-label'])
ab=soup.select('.player-cell a')

print(x)
hrefrow=soup.select('.player-cell a')
listPlayersProfile=[]
for i in range(0,x):
    if(hrefrow[i]['ga-label']!="TopCourt"):
        #print(hrefrow[i]['href'])
        listPlayersProfile.append(hrefrow[i]['href'])
print(listPlayersProfile)

print(playerList)

df1 = pd.DataFrame(list(zip(*[listPlayersProfile,listPlayers]))).add_prefix('href')
# writing the data into the file(
df1.to_csv('hrefList.csv', index=False)
