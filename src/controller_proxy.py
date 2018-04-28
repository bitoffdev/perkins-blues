import socket, pickle

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
    sys.stderr.write("Do not call this script!\n")
