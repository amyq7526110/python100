#!/usr/bin/env python3

import socket

host = ''  # 表示本机所有地址

port = 12345  # 应该大于1024

addr = (host,port)

s = socket.socket()  # 默认就是基于TCP的网络套接字

# 设置选项，程序结束之后可以立即运行，否则要等60秒

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

s.bind(addr)   # 绑定地址到套接字

s.listen(1)    # 启动监听进程

cli_sock, cli_addr = s.accept() # 等待客户端连接

print('Client connect from : ', cli_addr[0])

print(cli_sock.recv(1024))  #一次最多读1024字节数据

cli_sock.send(b' I am OK\r\n')  #发送的要求是bytes类型

cli_sock.close()

s.close()





