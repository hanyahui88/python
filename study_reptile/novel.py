# -*- coding: UTF-8 -*-
import urllib.request

response = urllib.request.urlopen("http://www.biqiuge.com/book/4772/")

print(response.read())
