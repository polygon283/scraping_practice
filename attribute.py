#属性でスクレイピング
from bs4 import BeautifulSoup
import requests

url = "https://www.orangepage.net/recipes/search/6"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

recipes = soup.find('div',id='recipe_list', class_='recipesList')
a_tag = recipes.find_all('a')
print([x['href'] for x in a_tag])