#! python3
# 2048.py - 2048のゲームをウェブで開いて、ランダムな矢印の入力を繰り返す

from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ウェブサイトを開く
browser = webdriver.Firefox()
browser.get("https://play2048.co")
html_elem = browser.find_element_by_tag_name("html")

# ランダムな矢印入力を繰り返す
while True:
    num = randint(1,4)
    if num == 1:
        html_elem.send_keys(Keys.UP)
    elif num == 2:
        html_elem.send_keys(Keys.DOWN)
    elif num == 3:
        html_elem.send_keys(Keys.RIGHT)
    else:
        html_elem.send_keys(Keys.LEFT)
    sleep(0.5)
