# -*- coding: UTF-8 -*-
import socket  # 导入 socket 模块

# 创建socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
hostname = socket.gethostname()
port = 9999

# 链接服务器
client.connect((hostname, port))
# 接受数据（小于1024的数据）
msg = client.recv(1024)
print(msg.decode())
client.close()
