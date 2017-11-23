# -*- coding: UTF-8 -*-
import socket
import sys

# 创建socket对象
serversocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
hostname = socket.gethostname()
port = 9999

# 绑定端口
serversocker.bind((hostname, port))

# 设置最大的连接数
serversocker.listen(5)

while True:
    # 建立客户端链接
    clientsocket, addr = serversocker.accept()
    print("链接地址：%s", str(addr))
    clientsocket.send("欢迎访问菜鸟".encode())
    clientsocket.close()
