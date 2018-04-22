#!/usr/env/bin python3
import socket, pickle, time
from fade_animation import FadeAnimation
from wipe_animation import WipeAnimation

class Controller:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _send(self, msg):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        totalsent = 0
        msgsize = len(msg)
        print("Sending %d bytes"%msgsize)
        msg = msgsize.to_bytes(2, byteorder='big') + msg
        while totalsent < msgsize:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
        self.sock.close()

    def add_animation(self, _animation):
        data = pickle.dumps(_animation)
        self._send(data)

if __name__ == "__main__":
    import sys
    control = Controller(sys.argv[1], int(sys.argv[2]))

    start = time.time()
    
    a1 = FadeAnimation(start + 1, start + 6,
            0.0, 0.5, 0x00ff00, 0x0000ff)
    control.add_animation(a1)

    a2 = FadeAnimation(start + 6, start + 10,
            0.0, 0.5, 0xff0000, 0x00ffff)
    control.add_animation(a2)

    a3 = FadeAnimation(start + 1, start + 4,
            0.5, 1.0, 0xff0000, 0x00ffff)
    control.add_animation(a3)
