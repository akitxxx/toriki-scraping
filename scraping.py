# -*- coding: utf-8 -*-


from selenium import webdriver
import pandas
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
browser = webdriver.Chrome(
    '/usr/local/Caskroom/chromedriver/74.0.3729.6/chromedriver')
# df = pandas.read_csv('default.csv', index_col=0)
url = "https://www.torikizoku.co.jp/menu/"

# メニューリスト
MENU_NAME_LIST = [u'焼鳥', u'逸品料理', u'スピードメニュー', u'ご飯もの／デザート', u'ドリンク']

# メニューリンク
menu_link = 'a.left-arrow'

browser.get(url)

# メニューリンクリストを取得
menu_link_list = browser.find_elements_by_css_selector(menu_link)

# スクレイピング処理


def scraping(menu, menu_name):
    if menu.text == menu_name:
        sleep(3)
        menu.click()
        sleep(3)

        title = browser.find_element_by_css_selector(
            'h4.yellowLineTitle').text
        print(title)

        item_list = browser.find_elements_by_css_selector('li h5')

        for item in item_list:
            print(item.text)


# 取得したいメニュー名と一致するメニューリンクにジャンプし、スクレイピング
for menu_name in MENU_NAME_LIST:
    for menu in menu_link_list:
        scraping(menu, menu_name)

browser.close()
