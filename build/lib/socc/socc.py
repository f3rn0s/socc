import socket
import telnetlib

class socc:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, message):
        if message[-1:] != "\n":
            message += "\n"
        self.socket.send(message.encode())

    def send_bytes(self, message):
        if message[-1:] != b"\n":
            message += b"\n"
        self.socket.send(message)

    def recv(self, amount=1024):
        return self.socket.recv(amount).decode()

    def recv_bytes(self, amount=1024):
        return self.socket.recv(amount)

    def ignore(self, number_of_lines=1, amount=1024):
        for i in range(0, number_of_lines):
            self.socket.recv(amount)

    def duplicate(self):
        return self.socket.dup()

    def interact(self):
        t = telnetlib.Telnet()
        t.sock = self.socket
        t.interact()

    def close(self):
        self.socket.close()
