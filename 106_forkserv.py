
import socket 
import os
from time import strftime()
    
class TcpTimeServer:
    def __init__(self, host='', port = 12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket,SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self,c_sock):
        while True:
            data = c_sock.recv(1024)
            if data.strip() == b'end'
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'),data.decode(utf8))                
            c_sock..send(data.encode('utf8'))
        c_sock.close()
    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            pid = os.fork()



            cli_sock, cli_addr = self.serv.accept

        
