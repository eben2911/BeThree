# Import Package requests and beautifulsoup
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Request from website 
page = requests.get("https://www.republika.co.id/")

# Extract content to object
obj = BeautifulSoup(page.text,"html.parser")

import json

data = []

now = datetime.now()
waktu = now.strftime("%d %B %Y %H:%M:%S")

f=open("D:\KAZUNO\Web\Project\Project-BETHREE\headline.json","w")
for headline in obj.find_all("div",class_="conten1"):
    data.append({
        "kategori":headline.find('h1').text, 
        "judul":headline.find('h2').text,
        "waktu_publish":headline.find('div',class_="date").text,
        "waktu_scrapping":waktu
        })

jdump=json.dumps(data)
f.writelines(jdump)
f.close()
