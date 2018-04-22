import socket, pickle, controller, sys
from threading import Thread

class InterfaceProxy:
    def __init__(self, host, port, control):
        self.control = control

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        serversocket.bind((host, port))
        # queue up to 5 requests
        serversocket.listen(20)

        while True:
            # establish a connection
            clientsocket,addr = serversocket.accept()

            print("Got a connection from %s" % str(addr))

            self._recv(clientsocket)
             
            msg = 'Thank you for connecting'+ "\r\n"
            clientsocket.send(msg.encode('ascii'))
            clientsocket.close()

    def _recv(self, clientsock):
        chunks = b''
        bytes_recd = 0
        msglen = clientsock.recv(2)
        msglen = int.from_bytes(msglen, byteorder='big') # largest value allowed
        while bytes_recd < msglen:
            chunk = clientsock.recv(min(msglen - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks += chunk
            bytes_recd = bytes_recd + len(chunk)
        obj = pickle.loads(chunks)
        self.control.add_animation(obj)

if __name__ == "__main__":
    control = controller.Controller()
    t1 = Thread(target=InterfaceProxy, args=(sys.argv[1],int(sys.argv[2]), control))
    t1.start()
    t2 = Thread(target=control.spin)
    t2.start()
