from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_path = '/Users/akaunntomei/Desktop/scraping_p/chromedriver'

#千代田図書館へ自動アクセス
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path,options=options)
url = 'https://www.library.chiyoda.tokyo.jp/'
driver.get(url)

sleep(2)

#検索欄に入力する
query = 'Pythonプログラミング'
search_box = driver.find_element_by_name('txt_word')
search_box.send_keys(query)

sleep(2)

#検索ボタンを押す
btn = driver.find_element_by_name('submit_btn_searchEasy')
btn.click()

sleep(5)

#検索結果を昇順にする
order = driver.find_element_by_id('opt_oder')
order_select = Select(order)
order_select.select_by_value('0')

sleep(3)

#昇順に変更した検索画面を再表示する
btn_sort = driver.find_element_by_name('submit_btn_sort')
btn_sort.click()