# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

'小说网站《笔趣看》URL：http://www.biqukan.com/ '
"""
静态爬取
爬虫的第一步，获取整个网页的HTML信息
爬虫的第二步，解析HTML信息提取我们感兴趣的内容
"""

"""
获取章节中的内容
"""


def content(target):
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html, "html.parser")
    texts = bf.find_all('div', class_="showtxt")
    return texts[0].text.replace('<div class="showtxt" id="content">', '').encode('utf-8')


"""
获取所有的章节链接
"""

topic = []


def pageHref():
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, "html.parser")
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]), "html.parser")
    a = a_bf.find_all('a')
    list = []
    for each in a:
        topic.append(each.string.encode('utf-8'))
        list.append(server + each.get('href'))
    return list


"""
写到文件中
"""


def writeFile(list):
    file = open("e:\\bbbbb.txt", "a", 1)
    try:
        for i in range(len(topic)):
            file.write(topic[i] + '\n')
            file.write(str(content(list[i])))
            file.write('\n\n')
            if i == 10:
                return
    except IOError, ex:
        print ex
    finally:
        file.close()


writeFile(pageHref())
