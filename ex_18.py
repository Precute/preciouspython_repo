import requests
from bs4 import BeautifulSoup
url  = 'http://data.pr4e.org/romeo.txt'
getpage = requests.get(url)
soup = BeautifulSoup(getpage.text, 'lxml')
soup
