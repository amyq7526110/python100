#!/usr/bin/env python3
import socket
from time import strftime

class Udpserver:
    def __init__(self, host = '', port = 12345):
        self.addr = (host,port)
        self.s = socket.socket(type=socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr)
    def rettime(self):
        while True:
            try:
                data, cli_addr = self.s.recvfrom(1024)
            except KeyboardInterrupt:
                break
            clock = strftime('%H:%M:%S')
            data = data.decode('utf8')
            data = '[%s] %s' % (clock,data) 
            self.s.sendto(data.encode('utf8'),cli_addr)
        self.s.close()

if __name__ == '__main__':
    s = Udpserver()
    s.rettime()
                    

        

