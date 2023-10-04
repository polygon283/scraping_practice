#id,classでスクレイピング
from bs4 import BeautifulSoup
import requests

url = "https://www.orangepage.net/recipes/search/6"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

recipes = soup.find('div',id='recipe_list', class_='recipesList')
p_tit_tags = recipes.find_all('h2', class_='tit')
print([x.string for x in p_tit_tags])