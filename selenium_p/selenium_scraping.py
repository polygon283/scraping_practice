from selenium import webdriver

driver = webdriver.Chrome('/Users/akaunntomei/Desktop/scraping_p/chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.library.chiyoda.tokyo.jp/')

#千代田図書館の開館、閉館のテキストを取得

schedule_els = driver.find_elements_by_class_name('schedule-list01__text')

#schedule_elsから一つずつ取り出しリストに格納
text = []
for s in schedule_els:
    text.append(s.text)

print(text)

driver.quit()
