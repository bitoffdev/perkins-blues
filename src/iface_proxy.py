# import controller, fade_animation, time
# from fade_animation import FadeAnimation
# import solid_animation
# from threading import Thread
# 
# control = controller.Controller()
# 
# def test(control):
#     time.sleep(0.5)
#     a1 = FadeAnimation(time.time() + 1,
#             time.time() + 8,
#             0.3, 0.8, 0x00ff00, 0x0000ff)
#     a2 = FadeAnimation(time.time() + 4,
#             time.time() + 8,
#             0.0, 0.3, 0x30f300, 0xff0044)
#     a3 = FadeAnimation(time.time() + 1,
#             time.time() + 4,
#             0.0, 0.3, 0xffff00, 0x0000ff)
#     control.add_animation(a1)
#     control.add_animation(a2)
#     control.add_animation(a3)
# 
# p = Thread(target=test, args=(control,))
# p.start()
# 
# control.spin()

import socket, pickle, controller
from threading import Thread

class InterfaceProxy:
    def __init__(self, host, port, control):
        self.control = control

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        serversocket.bind((host, port))
        # queue up to 5 requests
        serversocket.listen(5)

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
    import sys

    control = controller.Controller()
    # InterfaceProxy(sys.argv[1], int(sys.argv[2]))
    # p = Thread(target=InterfaceProxy, args=(sys.argv[1],int(sys.argv[2])))
    # p.start()
    # control.spin()
    p = Thread(target=control.spin)
    p.start()
    InterfaceProxy(sys.argv[1], int(sys.argv[2]), control)
