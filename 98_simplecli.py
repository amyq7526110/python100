#!/usr/bin/env python3
import socket

class Tcpclient:
    def __init__(self, host = '192.168.1.254', port = 12345):
        self.addr = (host , port)
        self.c = socket.socket()
        self.c.connect(self.addr)

    def  char(self):
        while True:
            data = input('> ') + '\r\n'
            self.c.send(data.encode('utf8')) 
            if data.strip() == 'end':
                break
            data = self.c.recv(1024)
            print(data.decode('utf8'))
        self.c.close()

if __name__ == '__main__':
    c = Tcpclient()
    c.char()
