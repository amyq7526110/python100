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

while True:
    cli_sock, cli_addr = s.accept() # 等待客户端连接
    print('Client connect from:',cli_addr)
    while True:
        data = cli_sock.recv(1024)
        print(data.decode('utf8'))   # bytes 类型转为string类型
        data = input('> ') + '\r\n'      # 获得的是string类型
        if data.strip()  == b'end':
            break
        cli_sock.send(data.encode('utf8'))  # 转化为bytes类型发送
    cli_sock.close()
s.close()





