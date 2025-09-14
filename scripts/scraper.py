
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

url='https://www.simplyhired.com/search?q=software+engineer'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 
webpage=requests.get(url ,headers=headers).text
# webpage=requests.get('https://www.simplyhired.com/search?q=software+engineer').text

print(webpage)

soup=BeautifulSoup(webpage,'lxml')
     

# print(soup.prettify())

print(soup.find_all('h2'))

