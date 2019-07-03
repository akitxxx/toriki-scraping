# -*- coding: utf-8 -*-

from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
browser = webdriver.Chrome(
    '/usr/local/Caskroom/chromedriver/75.0.3770.8/chromedriver')

# データフレーム
columns = ['name', 'class_id', 'classification']
df = pd.DataFrame(columns=columns)

# 鳥貴族メニューURL
url = "https://www.torikizoku.co.jp/menu/"

# メニューリスト
MENU_NAME_LIST = [[1, u'焼鳥'], [2, u'逸品料理'],
                  [3, u'スピードメニュー'], [4, u'ご飯もの／デザート'], [5, u'ドリンク']]

# メニューリンク
menu_link = 'a.left-arrow'

browser.get(url)

# スクレイピング処理


def scraping(menu_link_list, menu_name):
    for menu in menu_link_list:
        if menu.text == menu_name[1]:
            menu.click()
            # title = browser.find_element_by_css_selector(
            #     'h4.yellowLineTitle').text
            # print(title)

            item_list = browser.find_elements_by_css_selector('li h5')

            for item in item_list:
                se = pd.Series(
                    [item.text, menu_name[0], menu_name[1]], columns)
                global df
                df = df.append(se, columns)  # データフレームに行を追加
                print(item.text)

            print('\n')
            browser.get(url)
            break


# 取得したいメニュー名と一致するメニューリンクにジャンプし、スクレイピング
for menu_name in MENU_NAME_LIST:
    # メニューリンクリストを取得
    menu_link_list = browser.find_elements_by_css_selector(menu_link)
    scraping(menu_link_list, menu_name)

browser.close()

df.to_csv('./result.csv')
print('DONE...')
