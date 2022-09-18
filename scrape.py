
from bs4 import BeautifulSoup 
import requests
from csv import writer
from datetime import datetime
from Datadb import insertData,createConnection,createTable,getData

#create connection to DB
#create Table Data
# con = createConnection()
# con = createTable(con)

url = "https://www.theverge.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', {'class':'c-compact-river__entry'}) #c-entry-box--compact__body

dates = datetime.now().strftime('%d%m%Y')
Name = dates + "_verge.csv"

with open(Name,'w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['id', 'URL','headline', 'author', 'date']
    thewriter.writerow(header)

    i = 0
    for list in lists:
       
        id = i
        article_link = list.find("a").attrs['href']
        heading = list.find("h2").text
        try :
            author = list.find("span" ,class_="c-byline__author-name").contents[0]
        except:
            author = " "  
        try:
            date = list.find("time").attrs['datetime'][0:10]
        except:
            date = " "
        i += 1
        
        info = [id,article_link,heading,author,date]
        con = createConnection()
       
        data = insertData(info,con)

        getData(id,con)
        
        thewriter.writerow(info)

    