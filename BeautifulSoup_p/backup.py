# ライブラリをインポート
from time import sleep
import requests
from selenium import webdriver

# ChromeDriverのパスを指定
chrome_path = '/Users/akaunntomei/Desktop/scraping_p/chromedriver'

# WebDriverのインスタンスを作成、ChromeDriverのパスを指定
driver = webdriver.Chrome(chrome_path)

# ウェブページにアクセス
driver.get('https://www.library.chiyoda.tokyo.jp/')
sleep(5)
# ウェブページの要素を取得
schedule_el = driver.find_elements_by_class_name('schedule-list01__text')

# 要素の数を出力
print(len(schedule_el))

# テキストのリストを作成
text_list = []
for s in schedule_el:
    text_list.append(s.text)

print(text_list)
driver.quit()

# 出力（リスト内包表記をコメントアウトしています）
# print([s.text for s in schedule_el])