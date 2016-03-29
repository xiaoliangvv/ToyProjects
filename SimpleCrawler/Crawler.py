import requests
import lxml
from bs4 import BeautifulSoup

url = 'http://www.tripadvisor.cn/'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, "lxml")
cityNames = soup.select("#popularDestinations > div.section > ul.regionContent > li.active > ul > li > div.title > a.cityName")
for cityName in cityNames:
    print(cityName.get_text())
