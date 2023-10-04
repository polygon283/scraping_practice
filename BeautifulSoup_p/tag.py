#タグでスクレイピング
from bs4 import BeautifulSoup
import requests

url = "https://www.orangepage.net/recipes/search/6"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
h2_tags = soup.find_all('h2')
h2_string = [x.string for x in h2_tags]
print(h2_string)