# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup

"""
动态爬取
https://unsplash.com/图片爬取
"""


def getPic():
    target = "https://unsplash.com/"
    html = requests.get(target)
    print html.text


getPic()
