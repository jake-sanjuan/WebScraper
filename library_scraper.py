"""
Scrapes table on website https://publiclibraries.com/ to data list.  Will scrape any
state's library database on this site

Web scraper only useful for this particular site, made it to expedite a project I
was doing at work.
"""

from bs4 import BeautifulSoup
import requests

url = "https://publiclibraries.com/state/delaware/"

html_content = requests.get(url)

soup = BeautifulSoup(html_content.text, features="html.parser")

table = soup.find("table", attrs={"id": "libraries"})
table_data_header = table.find_all("th")
table_data = table.find_all("td")

headers = []
for element in table_data_header:
    headers.append(element.text.strip())

data = []
for element in table_data:
    data.append(element.text.strip())


