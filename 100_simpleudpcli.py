#!/usr/bin/env python3
import socket 

class Udpcli:
    def __init__(self, host = '192.168.1.254',port = 12345):
        self.addr = (host, port)
        self.c = socket.socket(type=socket.SOCK_DGRAM)

    def chat(self):
        while True: 
            data = input('> ')
            if data.strip() == 'end':
                break
            self.c.sendto(data.encode('utf8'), self.addr)
            print(self.c.recvfrom(1024)[0].decode('utf8'))
        self.c.close()                

if __name__ == '__main__':
    c = Udpcli()
    c.chat()


        



