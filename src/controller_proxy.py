#!/usr/env/bin python3
import socket, pickle, time
from fade_animation import FadeAnimation

MSGLEN = 316

class ControllerProxy:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def _send(self, msg):
        totalsent = 0
        msgsize = len(msg)
        print("Sending %d bytes"%msgsize)
        msg = msgsize.to_bytes(2, byteorder='big') + msg
        while totalsent < msgsize:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def add_animation(self, _animation):
        data = pickle.dumps(_animation)
        self._send(data)

if __name__ == "__main__":
    import sys
    control = ControllerProxy(sys.argv[1], int(sys.argv[2]))
    
    a1 = FadeAnimation(time.time() + 1,
            time.time() + 8,
            0.3, 0.8, 0x00ff00, 0x0000ff)
    control.add_animation(a1)
